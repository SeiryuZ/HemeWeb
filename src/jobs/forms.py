import os
import subprocess

from django import forms
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.core.files.base import ContentFile

from .models import Job

import requests


class ConfigureJobForm(forms.ModelForm):
    instance_type = forms.ChoiceField(widget=forms.Select,
                                      choices=Job.INSTANCE_CHOICES)
    container_image = forms.ChoiceField(widget=forms.Select,
                                        choices=Job.CONTAINER_CHOICES)

    class Meta:
        model = Job
        fields = ['instance_count']

    def __init__(self, *args, **kwargs):
        super(ConfigureJobForm, self).__init__(*args, **kwargs)

        # Sort based on the choice value, not index
        sorted_container_choices = sorted(Job.CONTAINER_CHOICES,
                                          key=lambda x: x[1],
                                          reverse=True)
        self.fields['container_image'].choices = sorted_container_choices

    def save(self, *args, **kwargs):
        kwargs['commit'] = False
        job = super(ConfigureJobForm, self).save(*args, **kwargs)
        job.instance_type = int(self.cleaned_data['instance_type'])
        job.container_image = int(self.cleaned_data['container_image'])
        job.save()
        return job


class RunJobSetupForm(forms.ModelForm):

    class Meta:
        model = Job
        fields = ['stl_file', 'profile_file']

    def __init__(self, *args, **kwargs):
        super(RunJobSetupForm, self).__init__(*args, **kwargs)
        self.fields['stl_file'].required = True
        self.fields['profile_file'].required = True

    def save(self, *args, **kwargs):
        kwargs['commit'] = False
        job = super(RunJobSetupForm, self).save(*args, **kwargs)
        job.prepare_directories()
        job.status = job.PREPROCESSING
        job.save()
        job.enqueue_setup()
        return job


class AddNewJobForm(forms.ModelForm):

    class Meta:
        model = Job
        fields = ['configuration_file', 'input_file']

    def __init__(self, *args, **kwargs):
        super(AddNewJobForm, self).__init__(*args, **kwargs)
        self.fields['configuration_file'].required = True
        self.fields['input_file'].required = True

    def save(self, *args, **kwargs):
        kwargs['commit'] = False
        job = super(AddNewJobForm, self).save(*args, **kwargs)
        job.prepare_directories()
        job.save()
        return job


class AddPreviousJobForm(forms.Form):
    job_id = forms.CharField(label=("Job ID (xxxxxxxx-xxx-xxx-xxxxxx):"))

    def clean_job_id(self):
        job_id = self.cleaned_data.get('job_id').strip()

        try:
            job = Job.objects.get(id=job_id)
            job.prepare_directories()

            # Refresh
            job = Job.objects.get(id=job_id)
            self.previous_job = job
            return job_id
        except (ValueError, ObjectDoesNotExist):
            pass

        raise forms.ValidationError("Previous job with id {} not found".format(job_id))

    def copy_file(self, old_file):
        new_file = ContentFile(old_file.read())
        new_file.name = os.path.basename(old_file.name)
        return new_file

    def copy_previous_job_config(self):
        job = Job.objects.create()
        job.prepare_directories()

        # Make duplicate, Ideally we could just link the .gmy because the .xml
        # Is the only file that can change between job execution
        job.configuration_file = self.copy_file(self.previous_job.configuration_file)
        job.input_file = self.copy_file(self.previous_job.input_file)
        job.instance_type = self.previous_job.instance_type
        job.instance_count = self.previous_job.instance_count
        job.container_image = self.previous_job.container_image

        job.save()
        return job


class AddPreviousJobFromURLForm(forms.Form):
    job_url = forms.URLField(
        label="Job url (https://zzz/yyyy/xx.tar.gz)"
    )

    # Taken from
    # http://stackoverflow.com/questions/16694907/how-to-download-large-file-in-python-with-requests-py
    def download_file(self, url):
        local_filename = url.split('/')[-1]

        # Because it is big, it should be streamed
        response = requests.get(url, stream=True)

        with open(local_filename, 'wb') as local_file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:  # filter out keep-alive new chunks
                    local_file.write(chunk)
                    #  f.flush() commented by recommendation from J.F.Sebastian

        return local_filename

    def clean(self, *args, **kwargs):
        cleaned_data = super(AddPreviousJobFromURLForm, self).clean(*args, **kwargs)

        # TODO: need to check whether download is successful or not
        # before proceeding
        self.download_file(cleaned_data['job_url'])

        return cleaned_data

    def copy_file(self, old_file):
        new_file = ContentFile(old_file.read())
        new_file.name = os.path.basename(old_file.name)
        return new_file

    def copy_previous_job_config(self):
        job_url = self.cleaned_data['job_url']
        local_filename = job_url.split('/')[-1]
        job_id = local_filename.strip('.tar.gz')

        # Uncompress
        cmd = 'sudo tar -xzf {} -C {}'.format(local_filename, settings.JOB_FILES_UPLOAD_DIR)
        subprocess.call(cmd, shell=True)

        # Delete compressed file
        cmd = 'sudo rm {}'.format(local_filename)
        subprocess.call(cmd, shell=True)

        previous_job, _ = Job.objects.get_or_create(id=job_id, defaults={'status': Job.PREVIOUS})

        # Link the appropriate instance attribute to the file
        previous_job.sync_files()
        previous_job = Job.objects.get(id=job_id)

        job = Job.objects.create()
        job.prepare_directories()

        # Make duplicate, Ideally we could just link the .gmy because the .xml
        # Is the only file that can change between job execution
        job.configuration_file = self.copy_file(self.previous_job.configuration_file)
        job.input_file = self.copy_file(self.previous_job.input_file)
        job.instance_type = self.previous_job.instance_type
        job.instance_count = self.previous_job.instance_count
        job.container_image = self.previous_job.container_image

        job.save()

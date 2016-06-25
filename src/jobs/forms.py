import os

from django import forms
from django.core.exceptions import ObjectDoesNotExist
from django.core.files.base import ContentFile

from .models import Job


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


class AddNewJobForm(forms.ModelForm):

    class Meta:
        model = Job
        fields = ['configuration_file', 'input_file']

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

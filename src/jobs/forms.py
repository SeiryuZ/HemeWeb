from django import forms

from .models import Job


class AddJobForm(forms.ModelForm):
    instance_type = forms.ChoiceField(widget=forms.Select,
                                      choices=Job.INSTANCE_CHOICES)

    class Meta:
        model = Job
        fields = ['configuration_file', 'input_file', 'instance_count']

    def save(self, *args, **kwargs):
        kwargs['commit'] = False
        job = super(AddJobForm, self).save(*args, **kwargs)
        job.instance_type = int(self.cleaned_data['instance_type'])
        job.save()
        return job

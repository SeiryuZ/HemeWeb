from django import forms

from .models import Job


class AddJobForm(forms.ModelForm):
    instance_type = forms.ChoiceField(widget=forms.Select,
                                      choices=Job.INSTANCE_CHOICES)

    class Meta:
        model = Job
        fields = ['configuration_file', 'input_file', 'instance_count']

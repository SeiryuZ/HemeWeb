from django import forms
from django.db import models


# Modified from https://gist.github.com/armonge/1093184
class ContentTypeRestrictedFileField(models.FileField):
    """
    Tomado de http://nemesisdesign.net/blog/coding/django-filefield-content-type-size-validation/
    Same as FileField, but you can specify:
        * content_types - list containing allowed content_types. Example: ['application/pdf', 'image/jpeg']
    """
    def __init__(self, *args, **kwargs):
        self.content_types = kwargs.pop("content_types", [])

        super(ContentTypeRestrictedFileField, self).__init__(*args, **kwargs)

    def clean(self, *args, **kwargs):
        data = super(ContentTypeRestrictedFileField, self).clean(*args, **kwargs)
        file = data.file
        try:
            content_type = file.content_type
            if content_type not in self.content_types:
                raise forms.ValidationError('Filetype not supported.')
        except AttributeError:
            pass
        return data

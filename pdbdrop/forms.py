
from django import forms

from pdbdrop.models import Upload


class UploadForm(forms.ModelForm):

    class Meta:
        model = Upload
        exclude = []

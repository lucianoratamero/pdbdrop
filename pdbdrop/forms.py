
from django import forms

from pdbdrop.models import Upload


class UploadForm(forms.ModelForm):
    upload_file = forms.FileField()

    class Meta:
        model = Upload
        exclude = ['file_path']

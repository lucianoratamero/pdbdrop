
from django import forms

from pdbdrop.models import Upload


class UploadForm(forms.ModelForm):
    upload_file = forms.FileField()
    video = forms.FileField(required=False)

    class Meta:
        model = Upload
        exclude = ['file_path', 'video_path']

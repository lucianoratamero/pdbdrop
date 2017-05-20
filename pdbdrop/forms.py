
from django import forms

from pdbdrop.models import Upload


class UploadForm(forms.ModelForm):
    upload_file = forms.FileField()
    video = forms.FileField(required=False)

    def clean_res(self):
        res_data = self.cleaned_data['res']
        if res_data and len(str(res_data)) < 3:
            raise forms.ValidationError('You need to pass at least two parameters to the res field')
        return res_data

    class Meta:
        model = Upload
        exclude = ['file_path', 'video_path']

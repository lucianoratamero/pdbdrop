
from django.views.generic.edit import FormView
from django.core.files.storage import FileSystemStorage

from pdbdrop.forms import UploadForm
from pdbdrop.use_cases import SpawnPdb2MovieProcessUseCase


class UploadView(FormView):
    form_class = UploadForm
    success_url = '/'
    template_name = 'upload.html'

    def form_valid(self, form):
        upload_model = form.save()
        uploaded_file = form.cleaned_data['upload_file']

        fs = FileSystemStorage()
        fs.base_location = 'uploaded_files'
        saved_file = fs.save(uploaded_file.name, uploaded_file.file)
        upload_model.file_path = fs.location + '/' + saved_file

        if form.cleaned_data['video']:
            video = form.cleaned_data['video']

            fs = FileSystemStorage()
            fs.base_location = 'uploaded_files'
            saved_file = fs.save(video.name, video.file)
            upload_model.video_path = fs.location + '/' + saved_file

        upload_model.save()

        use_case = SpawnPdb2MovieProcessUseCase(upload_model=upload_model)
        use_case.execute()

        return super(UploadView, self).form_valid(form)

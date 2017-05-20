
from django.views.generic.edit import FormView

from pdbdrop.forms import UploadForm


class UploadView(FormView):
    form_class = UploadForm
    success_url = '/'
    template_name = 'upload.html'

    def form_valid(self, form):
        form.save()
        return super(UploadView, self).form_valid(form)

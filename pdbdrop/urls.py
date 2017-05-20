
from django.conf.urls import url

from pdbdrop.views import UploadView


urlpatterns = [
    url(r'^', UploadView.as_view(), name='update'),
]

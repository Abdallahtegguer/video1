from django.urls import path
from cloud.views import Upload

app_name = 'demo'

urlpatterns = [
    path('', Upload.as_view(), name='upload'),
]
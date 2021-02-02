from . import views
from django.urls import path

app_name = "dropzone"

urlpatterns = [
    path('', views.homepage_view, name='homepage_view'),
]

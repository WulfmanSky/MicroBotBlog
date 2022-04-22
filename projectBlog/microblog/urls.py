from django.urls import path

from . import views

urlpatterns = [
    path('', views.project_overview, name='overview'),
    path('createPost', views.create_post, name='create_post'),
    path('createImagePost', views.download_image, name='download_image'),
    path('createVideoPost', views.download_video, name='download_video'),
    path('<str:project_name>', views.project_timeline, name='timeline')
]

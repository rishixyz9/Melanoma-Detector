from django.urls import path
from . import views

urlpatterns = [
    #home/
    path('', views.home, name='app-home'),
    #home/upload
    path('upload/', views.upload, name='app-upload'),
    #home/results
    path('results/', views.result, name='app-result'),
    #home/livefeed
    path('livefeed/', views.video, name='app-livefeed'),
    #For text on predicitve live imaging
    path('livepred/', views.video_feed, name='app-livepred')
]

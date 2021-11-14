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
    path('getcap/', views.getCap, name='app-getcap'),
    path('livefeed/', views.video, name='app-livefeed')
]

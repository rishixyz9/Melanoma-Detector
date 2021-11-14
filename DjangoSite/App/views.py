
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
from django.http import HttpResponse, request
from .forms import ImageForm
from .models import ImageModel

# Create your views here.
def home(request):
    return render(request, 'App/home.html')

def upload(request):
    if request.method == 'POST':
        uploaded_image = request.FILES['document']
        fs = FileSystemStorage()
        fs.save(uploaded_image.name, uploaded_image)
    return render(request, 'App/upload.html')

def result(request):
    return render(request, 'App/result.html')

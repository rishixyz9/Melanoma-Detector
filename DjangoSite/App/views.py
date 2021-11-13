from django.shortcuts import render
from django.http import HttpResponse, request
from .forms import ImageForm
from .models import ImageModel
from django.core.files.storage import FileSystemStorage

# Create your views here.
def home(request):
    return render(request, 'App/home.html')

def upload(request):
    if request.method == 'POST':
        uploaded_image = request.FILES['Image']
        fs = FileSystemStorage()
        fs.save(uploaded_image.name, uploaded_image)
    return render(request, 'App/upload.html')

def result(request):
    return HttpResponse("""<h1>Results Home</h1>""")
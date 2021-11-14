from django.shortcuts import render
from django.http import HttpResponse, request
from .forms import ImageForm
from .models import ImageModel
from django.core.files.storage import FileSystemStorage
from Tools.process import process

# Create your views here.
def home(request):
    return render (request, 'App/home.html')

def resultScreen(request, arg):
    result = process(arg['img_url'])
    arg['result'] = result[0]
    return render(request, 'App/result.html', arg)

def upload(request):
    context={}
    if request.method == 'POST':
        uploaded_image = request.FILES['Image']
        fs = FileSystemStorage()
        name = fs.save(uploaded_image.name, uploaded_image)
        context['img_url']=fs.url(name)
        return resultScreen(request, context)
    return render(request, 'App/upload.html')

def result(request):
    return HttpResponse("""<h1>Results Home</h1>""")

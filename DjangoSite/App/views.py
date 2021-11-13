from django.shortcuts import render
from django.http import HttpResponse, request

from Tools.process import process

# Create your views here.
def home(request):
    result = process()
    context = {
        'stats': result[0],
        'img_src': result[1], 
    }
    return render(request, 'App/home.html', context)
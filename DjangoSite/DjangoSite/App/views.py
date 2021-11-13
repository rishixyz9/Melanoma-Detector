from django.shortcuts import render
from django.http import HttpResponse, request

# Create your views here.
def home(request):
    return render(request, 'App/home.html')

def upload(request):
    return HttpResponse("""<h1>Upload Home</h1>""")

def result(request):
    return HttpResponse("""<h1>Results Home</h1>""")
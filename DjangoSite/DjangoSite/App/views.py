from django.shortcuts import render
from django.http import HttpResponse, request

# Create your views here.
def home(request):
    return render(request, 'App/home.html')
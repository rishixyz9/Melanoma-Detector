
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
from django.http import HttpResponse, request
from .forms import ImageForm
from .models import ImageModel
from .models import *
from django.core.mail import EmailMessage
from django.views.decorators import gzip
from django.http import StreamingHttpResponse
import cv2
import threading
from Tools.process import process
from Tools.process import init_model
from asgiref.sync import async_to_sync

# Create your views here.
def home(request):
    return render (request, 'App/home.html')

def resultScreen(request, arg):
    result = process(arg['img_url'])
    if result[0][0] == 1:
        arg['chance'] = 'You are at risk of having melanoma. Please see a doctor as soon as possible.'
    else:
        arg['chance'] = 'It seems you are not at risk of melanoma. Still consult a doctor as our diagnosis is not medical advise.'
    arg['result'] = result
    
    return render(request, 'App/result.html', arg)

def upload(request):
    context={}
    if request.method == 'POST':
        uploaded_image = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_image.name, uploaded_image)
        context['img_url']=fs.url(name)
        return resultScreen(request, context)
    return render(request, 'App/upload.html')

def result(request):
    return render(request, 'App/result.html')

def video(request):
    return render(request, 'App/livefeed.html')

#Below code courtesy of https://github.com/sawardekar/Django_VideoStream
def video_feed(request):
    return StreamingHttpResponse(gen(),
                    content_type='multipart/x-mixed-replace; boundary=frame')

#to capture video class
class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        (self.grabbed, self.frame) = self.video.read() # (did we get the image, the image)
        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.video.release()

    def get_frame(self):
        image = self.frame
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes(), jpeg

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()

def gen():
    camera = VideoCamera()
    model = init_model()
    while True:
        frame, jpeg = camera.get_frame()
        processed_str = str(model.process(jpeg))
        print(processed_str)
        #TODO figure out why it shows path to url and not text 
        #Possible idea convert text to image and stream img on html
        # we have a function that given nparray returns % chance of melanoma
        # number = random.randrange(1,100)
        yield (b'--frame\r\n'   
               b'Content-Type: text/plain\r\n\r\n' + processed_str + b'\r\n\r\n')
from django.shortcuts import render
from django.http import HttpResponse, request

import matplotlib.image as mpimage
from keras_preprocessing import image
import matplotlib.pyplot as plt
import numpy as np

import tensorflow as tf

# Create your views here.
def home(request):
    result = process()
    context = {
        'stats': result[0],
        'img_src': result[1], 
    }
    return render(request, 'App/home.html', context)

def process():
    loaded_model = tf.keras.models.load_model('ML_Model/fruit_classifier.h5')
    loaded_model.layers[0].input_shape

    image_path="ML_Model/apple.jpg"
    img = image.load_img(image_path, target_size=(200, 200))
    plt.imshow(img)
    img = np.expand_dims(img, axis=0)

    result=loaded_model.predict(img)
    obj = [result[0], image_path]
    return(obj)
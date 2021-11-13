import matplotlib.image as mpimage
from keras_preprocessing import image
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

def process():
    loaded_model = tf.keras.models.load_model('ML_Model/fruit_classifier.h5')
    loaded_model.layers[0].input_shape

    image_path="App/static/App/apple.jpg"
    img = image.load_img(image_path, target_size=(200, 200))
    plt.imshow(img)
    img = np.expand_dims(img, axis=0)

    result=loaded_model.predict(img)
    obj = [result[0], image_path]
    return(obj)
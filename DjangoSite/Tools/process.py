import matplotlib.image as mpimage
from keras_preprocessing import image
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

def process(image_path):
    image_path = './' + image_path
    loaded_model = tf.keras.models.load_model('ML_Model/MelanomaFinal.h5')
    loaded_model.layers[0].input_shape
    img = image.load_img(image_path, target_size=(224, 224))
    plt.imshow(img)
    img = np.expand_dims(img, axis=0)

    result=loaded_model.predict(img)
    obj = [result[0], image_path]
    return(obj)
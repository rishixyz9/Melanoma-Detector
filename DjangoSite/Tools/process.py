import matplotlib.image as mpimage
from keras_preprocessing import image
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from PIL import Image 

def process(image_path):
    image_path = '.' + image_path
    loaded_model = tf.keras.models.load_model('./ML_Model/finalfinal.h5')
    img = image.load_img(image_path, target_size=(224, 224))
    plt.imshow(img)
    img = np.expand_dims(img, axis=0)
    img = img/255
    result=loaded_model.predict(img)
    obj = [result[0], image_path]
    return(obj)

class init_model:
    def __init__(self) -> None:
        self.loaded_model = tf.keras.models.load_model('./ML_Model/MelanomaFinal.h5')
    def process(self, img):
        img.resize((224,224))
        img = np.expand_dims(img, axis=0)
        img = img/255
        result = self.loaded_model.predict(img)
        return result[0] # the chance that it's melanoma

if __name__ == '__main__':
    model = init_model()
    image_path = '../media/apple.jpg'
    img = image.load_img(image_path, target_size=(224, 224))
    ret = model.process(img)
    print(ret)
from django.shortcuts import render
from django.http import HttpResponse, request

# Create your views here.
def home(request):
<<<<<<< HEAD
    return render(request, 'App/home.html')
=======
    return render(request, 'App/home.html')

def upload(request):
    return HttpResponse("""<h1>Upload Home</h1>""")

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
>>>>>>> parent of d32cd1e (Revert "Merge branch 'main' of https://github.com/rishixyz9/HACKUTD-RKD")

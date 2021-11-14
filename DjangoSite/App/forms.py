from django import forms
 
class ImageForm(forms.Form):
    name = forms.CharField()
    image_field = forms.ImageField()
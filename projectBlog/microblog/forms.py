from django import forms
from .models import BlogImage,BlogVideo


class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = BlogImage
        fields = ('image')

class VideoForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = VideoImage
        fields = ('thumb','video')

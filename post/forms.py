from django import forms
from .models import Post
# djangoda formları class türünde tanımlıyoruz

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = [
            'title',
            'content',

        ]
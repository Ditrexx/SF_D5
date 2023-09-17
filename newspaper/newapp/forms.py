from django.forms import ModelForm
from .models import Post
from django import forms


# Создаём модельную форму
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['categoryType', 'author', 'title', 'text']
        widgets = {
            'categoryType': forms.Select(attrs={
                'class': 'form-control',
            }),
            'author': forms.Select(attrs={
                'class': 'form-control',
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter title'
            }),
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter text'
            }),
        }

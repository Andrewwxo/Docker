from django import forms
# from .models import Product


class MessageForm(forms.Form):
    theme = forms.CharField(label='Тема', widget=forms.TextInput(attrs={'class': 'form-control'}))
    text = forms.CharField(label='Текст', widget=forms.Textarea(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Ваша почта', widget=forms.EmailInput(attrs={'class': 'form-control'}))
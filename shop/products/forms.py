from django import forms


class MessageForm(forms.Form):
    theme = forms.CharField(label='Тема', widget=forms.TextInput(attrs={'class': 'form-control'}))
    text = forms.CharField(label='Текст', widget=forms.Textarea(attrs={'class': 'form-control'}))
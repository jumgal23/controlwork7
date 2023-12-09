from django import forms
from django.forms import widgets


class ArticleForm(forms.Form):
    name = forms.CharField(max_length=50, required=True, label="Имя автора")
    email = forms.EmailField(max_length=100, required=True, label='Почта автора')
    text = forms.CharField(max_length=3000, initial='Неизвестный', label="текст записи", widget=widgets.Textarea())


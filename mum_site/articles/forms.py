from .models import Articles
from django.forms import ModelForm, TextInput, DateInput, ClearableFileInput


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['category', 'sub_category','title', 'url', 'date']

        widgets ={
            'category': TextInput(attrs={
                'class': "form-control",
                'placeholder': "Категория"
            }),
            'sub_category': TextInput(attrs={
                'class': "form-control",
                'placeholder': "Подкатегория"
            }),
            'title': TextInput(attrs={
                'class': "form-control",
                'placeholder': "Название"
             }),
            'date': DateInput(attrs={
                'class': "form-control",
                'placeholder': "Дата добаления"
            }),
            'url': TextInput(attrs={
                'class': "form-control",
                'placeholder': "Ссылка на статью"
            }),
           # 'photo': ClearableFileInput(attrs={
               # 'class': "form-control",
                #'placeholder': "фото при необходимости"
           # }),

        }

from .models import Note
from django.forms import ModelForm, TextInput, DateInput, Textarea, ClearableFileInput


class NotesForm(ModelForm):
    class Meta:
        model = Note
        fields = ['category', 'sub_category', 'full_text', 'date']

        widgets ={
            'category': TextInput(attrs={
                'class': "form-control",
                'placeholder': "Категория"
            }),
            'sub_category': TextInput(attrs={
                'class': "form-control",
                'placeholder': "Подкатегория"
            }),
            'date': DateInput(attrs={
                'class': "form-control",
                'placeholder': "Дата добаления"
            }),
            'full_text': Textarea(attrs={
                'class': "form-control",
                'placeholder': "Основной текст"
            }),
           # 'photo': ClearableFileInput(attrs={
               # 'class': "form-control",
                #'placeholder': "фото при необходимости"
           # }),

        }
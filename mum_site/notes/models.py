from django.db import models

class Note(models.Model):
    category = models.CharField('Категория', max_length=50)
    sub_category = models.CharField('Подкатегория', max_length=250)
    full_text = models.TextField('Основной текст')
    date = models.DateField('Дата добаления')
    #photo = models.FileField('Фото/файл', blank=True)

    def __str__(self):
        return f'{self.category} -> {self.sub_category}'

    def get_absolute_url(self):
        return f'/notes/{self.id}'

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'

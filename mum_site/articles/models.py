from django.db import models

class Articles(models.Model):
    category = models.CharField('Категория',max_length=50)
    sub_category = models.CharField('Подкатегория', max_length=250)
    title = models.CharField('Название',  max_length=250)
    url = models.URLField('Ссылка')
    date = models.DateField('Дата добаления')

    def __str__(self):
        return f'{self.category} -> {self.sub_category}'

    def get_absolute_url(self):
        return self.url

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

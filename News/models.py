from django.db import models
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name='Контент')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата Создание')
    update_date = models.DateTimeField(auto_now=True, verbose_name='Дата изменение')
    photo = models.ImageField(upload_to='photos/%m%d', verbose_name='Фото', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Публиковано')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')

    def get_absolute_url(self):
        return reverse('news', kwargs={'news_id':self.pk})

    def __str__(self):
         return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-create_date']

class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Категория')

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id':self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']
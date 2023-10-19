from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField('Название поста', max_length=50)
    anons = models.CharField('Предпросмотр', max_length=255)
    text = models.TextField('Пост')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
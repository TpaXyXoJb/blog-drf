from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=256, unique=True)
    email = models.EmailField(unique=True)
    description = models.CharField('Описание', max_length=128, blank=True, null=True)
    image = models.ImageField('Фото профиля', upload_to='avatar', blank=True, null=True)

    def __str__(self):
        return self.username


class Category(models.Model):
    name = models.CharField('Название', max_length=128)

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField('Заголовок', max_length=128)
    description = models.CharField('Описание', max_length=256, blank=True, null=True)
    text = models.TextField('Текст', blank=True, null=True)
    image = models.ImageField('Изображение', upload_to='picture', blank=True, null=True)
    publish_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Автор')
    category = models.ManyToManyField(Category, verbose_name='Категория')

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField('Заголовок', max_length=128)
    description = models.CharField('Описание', max_length=256, blank=True, null=True)
    text = models.TextField('Текст', blank=True, null=True)
    image = models.ImageField('Изображение', upload_to='picture', blank=True, null=True)
    publish_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Автор')
    category = models.ManyToManyField(Category, verbose_name='Категория')

    def __str__(self):
        return self.title


class Review(models.Model):
    title = models.CharField('Заголовок', max_length=128)
    description = models.CharField('Описание', max_length=256, blank=True, null=True)
    text = models.TextField('Текст', blank=True, null=True)
    image = models.ImageField('Изображение', upload_to='picture', blank=True, null=True)
    publish_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Автор')
    category = models.ManyToManyField(Category, verbose_name='Категория')

    def __str__(self):
        return self.title

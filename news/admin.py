from django.contrib import admin
from .models import User, News, Article, Review, Category


# Register your models here.
admin.site.register(User)
admin.site.register(News)
admin.site.register(Article)
admin.site.register(Review)
admin.site.register(Category)

from django.contrib import admin
from .models import Publisher, Author, Genre, Category, Book

# Регистратция моделей
admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Category)
admin.site.register(Book)
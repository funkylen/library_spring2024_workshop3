from django.contrib import admin
from books import models

# Register your models here.

admin.site.register(models.Author)
admin.site.register(models.Book)
admin.site.register(models.BookInstance)
admin.site.register(models.Genre)
admin.site.register(models.Profile)

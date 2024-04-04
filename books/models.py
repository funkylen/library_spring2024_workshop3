from django.db import models
from django.contrib.auth.models import User
from datetime import date


class AuthorManager(models.Manager):
    def get_alive(self):
        return self.filter(death_date__isnull=True)

    def get_young(self):
        return self.filter(birth_date__gte=date(2000, 1, 1))


class Author(models.Model):
    name = models.CharField(max_length=255)
    birth_date = models.DateField()
    death_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = AuthorManager()

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=255)
    genres = models.ManyToManyField(Genre, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class BookInstance(models.Model):
    STATUS_CHOICES = [("a", "Available"), ("na", "Not Available")]
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS_CHOICES, max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.book.name} {self.get_status_display()}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    avatar = models.ImageField(null=True, blank=True)

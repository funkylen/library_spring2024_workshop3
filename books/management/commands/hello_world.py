from django.core.management.base import BaseCommand, CommandError
from books.models import Book


class Command(BaseCommand):
    def handle(self, *args, **options):
        books = Book.objects.all()

        for book in books:
            print(book)

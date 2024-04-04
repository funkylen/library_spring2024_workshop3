from django.shortcuts import render
from books.models import Author
from django.db.models import Count

# Create your views here.


def index(request):
    authors = Author.objects.annotate(num_books=Count('book')).all()

    context = {"authors": authors}

    return render(request, "index.html", context)

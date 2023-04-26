from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Author, BookInstance, Genre

# Create your views here.
def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    num_authors = Author.objects.count()

    num_instances_available = BookInstance.objects.filter(status__exact='g').count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }

    return render(request, 'index.html', context=context)
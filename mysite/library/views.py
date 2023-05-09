from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Author, BookInstance, Genre
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.core.paginator import Paginator


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


def authors(request):
    paginator = Paginator(Author.objects.all(), 3)
    page_number = request.GET.get('page')
    paged_authors = paginator.get_page(page_number)
    context = {
        'authors': paged_authors
    }
    return render(request, 'authors.html', context=context)


def author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    context = {
        'author': author,
    }
    return render(request, 'author.html', context=context)


class BookListView(generic.ListView):
    model = Book
    paginate_by = 3
    context_object_name = 'books'
    template_name = "books.html"

class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'book.html'
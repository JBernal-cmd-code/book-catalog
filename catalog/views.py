from django.views.generic import ListView
from .models import Publisher, Book, Review

class PublisherListView(ListView):
    model = Publisher
    template_name = 'catalog/publisher_list.html'

class BookListView(ListView):
    model = Book
    template_name = 'catalog/book_list.html'

class ReviewListView(ListView):
    model = Review
    template_name = 'catalog/review_list.html'

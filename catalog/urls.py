from django.urls import path
from .views import PublisherListView, BookListView, ReviewListView

urlpatterns = [
    path('publishers/', PublisherListView.as_view(), name='publisher_list'),
    path('', BookListView.as_view(), name='book_list'),
    path('reviews/', ReviewListView.as_view(), name='review_list'),
]
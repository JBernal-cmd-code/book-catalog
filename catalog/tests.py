from django.test import TestCase
from django.urls import reverse
from .models import Book, Publisher


class BookModelTest(TestCase):
    def test_book_name(self):
        publisher = Publisher.objects.create(name='Publishing House')
        book_title = 'The Dog Story'
        Book.objects.create(
            title=book_title,
            publisher=publisher,
            publication_date='2023-01-01'
        )
        
        # Indented inside the test method
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, book_title)
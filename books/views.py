from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from books.models import Book


def main(request):
    # Отримати всі книги за 2023 рік з вашого джерела даних
    books = Book.objects.filter(year=2023)

    context = {
        'books': books
    }

    return render(request, 'main.html', context)

def book_detail(request, book_id):
    # Отримати конкретну книгу за її ідентифікатором
    book = Book.objects.get(id=book_id)

    context = {
        'book': book
    }

    return render(request, 'book_detail.html', context)

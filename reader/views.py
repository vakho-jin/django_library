from django.shortcuts import render, get_object_or_404
from book.models import Book

def success_page(request, pk):
    book = get_object_or_404(Book, pk = pk)
    return render(request, 'success.html', {'book': book})
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from reader.forms import ReaderForm

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk = pk)
    if request.method == 'POST':
        form = ReaderForm(request.POST)
        if form.is_valid():
            reader = form.save(commit = False)
            reader.book = book
            reader.save()
            return redirect('success_page', pk = book.pk)
    else:
        form = ReaderForm()
    return render(request, 'book_detail.html', {'book': book, 'form': form})
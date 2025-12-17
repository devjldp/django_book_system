from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Book
from .forms import BookForm

# Create your views here.

def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book created successfully!')
            return redirect('book_list')
    else:
        form = BookForm()

    context = {
        'form': form,
        'action': 'Create'
    }
    return render(request, 'books/add_book.html', context )

def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    print(pk)
    print(book)
    print(request.method)
    if request.method == 'POST':
        book.delete()
        messages.success(request, 'Book deleted successfully!')
        return redirect('book_list')
    return redirect('book_list')
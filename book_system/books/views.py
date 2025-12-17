from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Book
from .forms import BookForm

# Create your views here.

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
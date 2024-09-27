from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, BorrowedBook
from .forms import BookForm
from django.utils import timezone

def book_list(request):
    books = Book.objects.all()

    context = {
        'books': books
    }
    return render(request, 'BooksManagement/books_list.html', context)


def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book:book_list')

    else:
        form = BookForm()
    return render(request, 'BooksManagement/book_create.html', {'form': form})


def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book:book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'BooksManagement/book_update.html', {'form': form})


def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect('book:book_list')
    return render(request, 'BooksManagement/book_delete.html', {'book': book})


def borrow_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    
    if request.method == 'POST':
        if book.is_available:
            borrowed_book = BorrowedBook(user=request.user, book=book)
            borrowed_book.save()
            book.is_available = False
            book.save()
            return redirect('book:book_list')

    return render(request, 'BooksManagement/borrow_book.html', {'book': book})

def return_book(request, pk):
    borrowed_book = get_object_or_404(BorrowedBook, pk=pk)

    if request.method == 'POST':
        borrowed_book.return_date = timezone.now().date()
        borrowed_book.status = 'returned'
        borrowed_book.book.is_available = True
        borrowed_book.book.save()
        borrowed_book.save()
        return redirect('book:borrowed_books_list')

    return render(request, 'BooksManagement/return_book.html', {'borrowed_book': borrowed_book})


def borrowed_books_list(request):
    borrowed_books = BorrowedBook.objects.filter(user=request.user)

    context = {
        'borrowed_books': borrowed_books
    }
    return render(request, 'BooksManagement/borrowed_books_list.html', context)
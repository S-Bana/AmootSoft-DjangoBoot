from .views import book_list, book_create, book_update, book_delete, borrow_book, return_book, borrowed_books_list
from django.urls import path

app_name = 'book'

urlpatterns = [
    path('', book_list, name='book_list'),
    path('create/book/', book_create, name='book_create'),
    path('update/book/<int:pk>/', book_update, name='book_update'),
    path('delete/book/<int:pk>/', book_delete, name='book_delete'),
    
    path('borrow/<int:pk>/', borrow_book, name='borrow_book'),
    path('return/<int:pk>/', return_book, name='return_book'),
    path('my-borrowed-books/', borrowed_books_list, name='borrowed_books_list'),
]

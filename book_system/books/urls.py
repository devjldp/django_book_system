from django.urls import path
from . import views

urlpatterns = [
    path('add', views.book_create, name="add_book"),
    path('list', views.book_list, name="book_list"),
    path('list', views.book_delete, name="book_delete"),
]
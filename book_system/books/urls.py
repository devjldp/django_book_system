from django.urls import path
from . import views

urlpatterns = [
    path('add', views.book_create, name="add_book"),
]
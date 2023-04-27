from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("authors/", views.authors, name="authors"),
    path("authors/<int:author_id>", views.author, name="author"),
]
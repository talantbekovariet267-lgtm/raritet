from django.urls import path
from .views import main_page, contacts_page, about_page, books_page, movies_page, random_number


urlpatterns = [
    path("", main_page, name="main_page"),
    path("contacts/", contacts_page, name="contast_page"),
    path("about/", about_page, name="about_page"),
    path("books/", books_page, name="books_page"),
    path("movies/", movies_page, name="movies_page"),
    path("random/", random_number, name="random_number"),
]
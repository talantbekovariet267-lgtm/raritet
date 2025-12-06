from django.shortcuts import render, HttpResponse

books = [
    {
        "title": "1984",
        "rating": 9.7,
        "cover_url": "https://images.booksense.com/images/333/869/9781328869333.jpg",
        "wiki_url": "https://en.wikipedia.org/wiki/Nineteen_Eighty-Four"
    },
    {
        "title": "Brave New World",
        "rating": 9.4,
        "cover_url": "https://upload.wikimedia.org/wikipedia/en/6/62/BraveNewWorld_FirstEdition.jpg",
        "wiki_url": "https://en.wikipedia.org/wiki/Brave_New_World"
    },
    {
        "title": "To Kill a Mockingbird",
        "rating": 9.6,
        "cover_url": "https://upload.wikimedia.org/wikipedia/commons/4/4f/To_Kill_a_Mockingbird_%28first_edition_cover%29.jpg",
        "wiki_url": "https://en.wikipedia.org/wiki/To_Kill_a_Mockingbird"
    },
    {
        "title": "The Great Gatsby",
        "rating": 9.3,
        "cover_url": "https://i0.wp.com/americanwritersmuseum.org/wp-content/uploads/2018/02/CK-3.jpg?resize=267%2C400&ssl=1",
        "wiki_url": "https://en.wikipedia.org/wiki/The_Great_Gatsby"
    },
    {
        "title": "The Catcher in the Rye",
        "rating": 8.9,
        "cover_url": "https://upload.wikimedia.org/wikipedia/commons/8/89/The_Catcher_in_the_Rye_%281951%2C_first_edition_cover%29.jpg",
        "wiki_url": "https://en.wikipedia.org/wiki/The_Catcher_in_the_Rye"
    },
    {
        "title": "Crime and Punishment",
        "rating": 9.8,
        "cover_url": "https://m.media-amazon.com/images/I/612KmKeEYEL._AC_UF1000,1000_QL80_.jpg",
        "wiki_url": "https://en.wikipedia.org/wiki/Crime_and_Punishment"
    },
    {
        "title": "The Lord of the Rings",
        "rating": 9.9,
        "cover_url": "https://m.media-amazon.com/images/I/7125+5E40JL._AC_UF1000,1000_QL80_.jpg",
        "wiki_url": "https://en.wikipedia.org/wiki/The_Lord_of_the_Rings"
    },
    {
        "title": "The Hobbit",
        "rating": 9.5,
        "cover_url": "https://m.media-amazon.com/images/I/712cDO7d73L._AC_UF1000,1000_QL80_.jpg",
        "wiki_url": "https://en.wikipedia.org/wiki/The_Hobbit"
    },
    {
        "title": "Fahrenheit 451",
        "rating": 9.2,
        "cover_url": "https://d28hgpri8am2if.cloudfront.net/book_images/onix/cvr9781451673265/fahrenheit-451-9781451673265_hr.jpg",
        "wiki_url": "https://en.wikipedia.org/wiki/Fahrenheit_451"
    },
    {
        "title": "The Little Prince",
        "rating": 9.7,
        "cover_url": "https://m.media-amazon.com/images/I/71OZY035QKL.jpg",
        "wiki_url": "https://en.wikipedia.org/wiki/The_Little_Prince"
    }
]

# Для отображения HTML-страниц используется функция render
# return render(request, 'название_файла.html', {})

def main_page(request):
    return render(request, 'index.html', {})

def contacts_page(request):
    return HttpResponse("<h>Мой номер телефона: +996 777 999 666</H1>")

def about_page(request):
    import random

    names = ["Adilet", "Akibek", "Stalbek"]
    random_number = random.randint(1, 100)

    context = {
        'names': names,
        'random_number': random_number,
        'is_even': random_number % 2 == 0
    }

    return render(request, 'about_page.html', context)

def books_page(request):
    context = {'books': books}
    return render(request, 'books_page.html', context)

def movies_page(request):
    movies = [
        {"title": "Inception", "rating": 8.8, "year": 2010},
        {"title": "Interstellar", "rating": 8.6, "year": 2014},
        {"title": "The Matrix", "rating": 8.7, "year": 1999},
    ]
    context = {'movies': movies}
    return render(request, 'movies_page.html', context)


def random_number(request):
    import random
    x = random.randint(1, 6)
    context = {'x': x}
    return render(request, 'random_number.html', context)
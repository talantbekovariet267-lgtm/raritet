from django.db import models

class Publisher(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название издателия")
    founding_date = models.DateField(max_length=150, verbose_name="Дата основания")

    class Meta:
        verbose_name = "Издатель"
        verbose_name_plural = "Издатели"


    def __str__(self):
        return f"{self.name} ({self.founding_date})"
    
class Author(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    middle_name = models.CharField(max_length=250, null=True, blank=True)
    father_name = models.CharField(max_length=250, null=True, blank=True)
    dade_of_birth = models.DateField()
    dade_of_birth = models.DateField(null=True, blank=True)
    biography = models.TextField(max_length=40000)


    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"



    def __str__(self):
        name = []
        names = [self.first_name, self.middle_name, self.last_name, self.father_name]
        
        for n in names:
            if n:
                name.append(n)

        result = f"{' '.join(name)} ({self.dade_of_birth})"

        if self.dade_of_birth:
            result += f" - ({self.dade_of_birth})"

        return result
    
class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название катагории")
    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "катогории"
       
    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название жанра")

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"
       

    def __str__(self):
        return self.name


class Book(models.Model):
    COVER_TYPES = (
        ('soft', 'Мягкая обложка'),
        ('hard', 'Твердая обложка'),
    )

    name = models.CharField(max_length=255, verbose_name="Название издателия" )
    price = models.PositiveBigIntegerField(verbose_name="Цена")
    description = models.TextField(max_length=2000, verbose_name="Описание")
    cover_type = models.CharField(choices=COVER_TYPES, max_length=16, verbose_name="Тип обложки")
    release_date = models.DateField(verbose_name="Дата выхода")
    page_count = models.PositiveBigIntegerField(verbose_name="кол-во страниц")


    author = models.ManyToManyField(Author, verbose_name = "Автор" )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name = "Катагория")
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, verbose_name = "Издатель")
    genre = models.ManyToManyField(Genre, verbose_name = "Жанр")


    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"


    def _str_(self):
        return f"{self.name} ({self.release_date})"
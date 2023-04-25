import uuid as uuid
from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(verbose_name="Pavadinimas", max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Zanras"
        verbose_name_plural = "Zanrai"



class Author(models.Model):
    first_name = models.CharField("Vardas", max_length=50)
    last_name = models.CharField("Pavarde", max_length=50)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Autorius"
        verbose_name_plural = "Autoriai"


class Book(models.Model):
    title = models.CharField(verbose_name="Pavadinimas", max_length=100)
    summary = models.TextField(verbose_name="Aprasymas")
    isbn = models.CharField(verbose_name="ISBN", max_length=13)
    author = models.ForeignKey(to="Author", verbose_name="Autorius", on_delete=models.SET_NULL, null=True, blank=True)
    genre = models.ManyToManyField(to="Genre", verbose_name="Zanras")

    def __str__(self):
        return f"{self.title} {self.author}"
    class Meta:
        verbose_name = "Knyga"
        verbose_name_plural = "Knygos"

    def display_genre(self):
        return ', '.join(genre.name for genre in self.genre.all())

    display_genre.short_description = 'Žanras'


class BookInstance(models.Model):
    book = models.ForeignKey(to="Book", verbose_name="Knyga", on_delete=models.CASCADE)
    uuid = models.UUIDField(default=uuid.uuid4)
    due_back = models.DateField(verbose_name="Bus prieinama", null=True, blank=True)

    LOAN_STATUS = (
        ('a', 'Administruojama'),
        ('p', 'Paimta'),
        ('g', 'Galima paimti'),
        ('r', 'Rezervuota'),
    )

    status = models.CharField(
        verbose_name="Busena",
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='a',
    )

    def __str__(self):
        return f"{self.book.title}: {self.uuid} ({self.due_back} - {self.status})"

    class Meta:
        verbose_name = "Knygos egzempliorius"
        verbose_name_plural = "Knygos egzemplioriai"
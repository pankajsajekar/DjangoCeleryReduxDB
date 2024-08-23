from django.db import models

class Author(models.Model):
    author_name = models.CharField(("Author"), max_length=50)
    city = models.CharField(("city"), max_length=50, blank=True)

class Book(models.Model):
    book_name = models.CharField(("Book Name"), max_length=50)
    launchdate = models.DateField(("Lunch Date"), auto_now=False, auto_now_add=True, )
    author = models.ManyToManyField(Author, related_name='author', blank=True)

from django.db import models
from book.models import Book

class Reader(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    phone = models.CharField(max_length = 20)
    book = models.ForeignKey(Book, on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.book.title}"
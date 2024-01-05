from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13)
    image = models.ImageField(upload_to="image", default='templates/books/IMG_2181.jpg')



    def __str__(self) -> str:
        return self.title
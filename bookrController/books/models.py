from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


class Publication(models.Model):
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=25, validators=[RegexValidator(r'^\d{1,25}$', 'ISBN must contain only numbers.')])
    imagePath = models.CharField(max_length=1000, default="https://uruguaj.com/nn.jpeg")

    class Meta:
        abstract = True

    def __str__(self):
        return self.title

class Book(Publication):
    def __str__(self):
        return f"Book: {self.title}"
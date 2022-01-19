from django.db import models

# Create your models here.
from django.db import models


class Person(models.Model):
    name = models.CharField("Им'я", max_length=30)

    def __str__(self):
        return self.name

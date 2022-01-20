from django.db import models

# Create your models here.
from django.db import models


class Person(models.Model):
    first_name = models.CharField("Им'я", max_length=30)
    last_name = models.CharField("Призвіще", max_length=30)

    def __str__(self):
        return self.first_name + self.last_name

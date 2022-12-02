from django.db import models

# Create your models here.


class Author(models.Model):
    id = models.IntegerField(primary_key=True)
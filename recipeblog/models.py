from django.db import models

# Create your models here.


class User(models.Model):
    ACTIVE = 'AC'
    BLOCKED = 'BL'
    status_choices = [
        (ACTIVE, 'Active'),
        (BLOCKED, 'Blocked')
    ]
    username = models.CharField(unique=True, max_length=25)
    status = models.CharField(max_length=2, choices=status_choices, default=ACTIVE)
    faves = models.TextField(default='')
    registration_date = models.DateTimeField(auto_now_add=True, editable=False)
    update_date = models.DateTimeField(auto_now=True)


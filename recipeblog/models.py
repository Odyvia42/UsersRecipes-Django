from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(unique=True, max_length=25)
    ACTIVE = 'AC'
    BLOCKED = 'BL'
    status_choices = [
        (ACTIVE, 'Active'),
        (BLOCKED, 'Blocked')
    ]
    status = models.CharField(max_length=2, choices=status_choices, default=ACTIVE)
    faves = models.TextField(default='')
    registration_date = models.DateTimeField(auto_now_add=True, editable=False)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

class Recipe(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    publication_date = models.DateTimeField(auto_now_add=True, editable=False)
    update_date = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=50)
    SALAD = 'SL'
    FIRST_COURSE = 'FC'
    MAIN_COURSE = 'MC'
    DESSERT = 'DS'
    BEVERAGE = 'BV'
    BAKERY = 'BK'
    dish_type_choices = [
        (SALAD, 'Salad'),
        (FIRST_COURSE, 'First course'),
        (MAIN_COURSE, 'Main course'),
        (DESSERT, 'Dessert'),
        (BEVERAGE, 'Beverage'),
        (BAKERY, 'Bakery'),
    ]
    dish_type = models.CharField(max_length=2, choices=dish_type_choices, default=SALAD)
    description = models.TextField
    steps_to_complete = models.TextField
    picture = models.URLField
    likes = models.IntegerField
    tags = models.CharField(max_length=150)
    ACTIVE = 'AC'
    BLOCKED = 'BL'
    status_choices = [
        (ACTIVE, 'Active'),
        (BLOCKED, 'Blocked')
    ]
    status = models.CharField(max_length=2, choices=status_choices, default=ACTIVE)

    def __str__(self):
        return self.title


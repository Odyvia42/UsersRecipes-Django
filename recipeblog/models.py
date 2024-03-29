from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager


# Create your models here.


class User(AbstractUser):
    username = models.CharField(unique=True, max_length=25)
    ACTIVE = 'AC'
    BLOCKED = 'BL'
    status_choices = [
        (ACTIVE, 'Active'),
        (BLOCKED, 'Blocked')
    ]
    status = models.CharField(max_length=2, choices=status_choices, default=ACTIVE)
    registration_date = models.DateTimeField(auto_now_add=True, editable=False)
    update_date = models.DateTimeField(auto_now=True)

    password = models.CharField(max_length=350)
    email = models.EmailField()

    class Meta:
        ordering = ['registration_date']

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('user-detail', args=[str(self.id)])


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
        (SALAD, 'Салат'),
        (FIRST_COURSE, 'Первое'),
        (MAIN_COURSE, 'Второе'),
        (DESSERT, 'Десерт'),
        (BEVERAGE, 'Напиток'),
        (BAKERY, 'Выпечка'),
    ]
    dish_type = models.CharField(max_length=2, choices=dish_type_choices, default=SALAD)
    description = models.TextField(default='')
    ingredients = models.TextField(default='')
    steps_to_complete = models.TextField(default='')
    picture = models.URLField(default='')
    likes = models.ManyToManyField(User, related_name='recipe_likes')
    favs = models.ManyToManyField(User, related_name='recipe_favs', blank=True)
    tags = TaggableManager(help_text='Введите теги через запятую', blank=True)
    ACTIVE = 'AC'
    BLOCKED = 'BL'
    status_choices = [
        (ACTIVE, 'Active'),
        (BLOCKED, 'Blocked')
    ]
    status = models.CharField(max_length=2, choices=status_choices, default=ACTIVE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('recipe-detail', args=[str(self.id)])

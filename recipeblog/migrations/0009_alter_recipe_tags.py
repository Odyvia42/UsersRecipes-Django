# Generated by Django 4.1.3 on 2023-04-06 04:10

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        ('recipeblog', '0008_remove_recipe_tags_recipe_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='Введите теги через запятую', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]

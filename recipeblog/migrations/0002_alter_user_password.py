# Generated by Django 4.1.3 on 2023-03-10 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipeblog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=350),
        ),
    ]

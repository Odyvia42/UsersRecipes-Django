# Generated by Django 4.1.3 on 2023-03-08 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipeblog', '0006_alter_user_managers_user_date_joined_user_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=50),
        ),
    ]

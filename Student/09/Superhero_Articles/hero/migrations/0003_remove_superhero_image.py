# Generated by Django 4.0.4 on 2022-11-04 21:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0002_superhero_description_superhero_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='superhero',
            name='image',
        ),
    ]

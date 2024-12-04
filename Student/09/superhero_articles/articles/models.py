from django.db import models
from django.contrib.auth.models import User

class Superhero(models.Model):
    name = models.CharField(max_length=100)
    identity = models.CharField(max_length=100)
    description = models.TextField()
    strength = models.CharField(max_length=100)
    weakness = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
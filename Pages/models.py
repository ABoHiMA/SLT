from django.db import models

# Create your models here.

class Feedback(models.Model):
    username = models.CharField(max_length=1806)
    text = models.TextField()
    def __str__(self):
      return self.username


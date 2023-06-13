from django.db import models
# from django.db.models import Model
# import uuid

# Create your models here.

class Image(models.Model):
    image_file = models.ImageField(upload_to='images/')
    letter = models.CharField(max_length=1)
    def __str__(self):
      return self.letter
                  

from django.db import models


# Create your models here.

class Screenshot(models.Model):
    datetime = models.DateField(auto_now=True)
    image = models.ImageField(upload_to='images/')
    #
    # def __str__(self):
    #     return self.datetime

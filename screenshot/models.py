from django.db import models


# Create your models here.

class Screenshot(models.Model):
    datetime = models.DateTimeField(auto_now=True)
    #전처리 전 임시폴더에 저장
    image = models.ImageField(upload_to='images/temp')
    #
    # def __str__(self):
    #     return self.datetime

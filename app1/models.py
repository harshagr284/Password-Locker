from django.db import models
from django.urls import reverse
class Password1(models.Model):
    title=models.CharField(max_length=264)
    password=models.CharField(max_length=264)
    def get_absolute_url(self):
        return reverse("detail",kwargs={'pk':self.pk})


# Create your models here.

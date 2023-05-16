from django.db import models

# Create your models here.

class Carousal(models.Model):
    image = models.ImageField(upload_to='carousal')
    title = models.CharField(max_length=225)
    sub_title = models.CharField(max_length=500)
    button_label = models.CharField(max_length=150)
    button_url = models.CharField(max_length=100)

    def __str__(self):
        return self.title
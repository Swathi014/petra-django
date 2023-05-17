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

class Category(models.Model):
    image = models.ImageField(upload_to='category')
    title = models.CharField(max_length=225)
    inner_title = models.CharField(max_length=500)
    inner_subtitle = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.title

class Product(models.Model):
    image = models.ImageField(upload_to='product')
    title = models.CharField(max_length=225)
    description = models.CharField(max_length=225)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Abouthome(models.Model):
    title = models.CharField(max_length=225)
    sub_title = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.title    
    
class Logo_slider(models.Model):
    image = models.ImageField(upload_to='logo_slider')

    # def __str__(self):
    #     return self.image

   
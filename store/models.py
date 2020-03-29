from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=30)
    price = models.IntegerField()
    description = models.TextField()
    img = models.ImageField(upload_to='images/')
    seller = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

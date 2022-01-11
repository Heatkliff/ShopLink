from django.db import models


class ProductPhoto(models.Model):
    image = models.ImageField(upload_to='./products')

    def __str__(self):
        return f"{self.image.path}"


class Product(models.Model):
    title = models.CharField(max_length=100, blank=True)
    description = models.TextField(max_length=500)
    photos = models.ForeignKey(ProductPhoto, on_delete=models.DO_NOTHING)
    price = models.FloatField(blank=False, default=0.0)

    def __str__(self):
        return f"{self.title} : {self.price}"

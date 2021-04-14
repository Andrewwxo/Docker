from django.db import models


# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name


class Kind(models.Model):
    name = models.CharField(max_length=32, unique=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='kind')





class Weight(models.Model):
    name = models.IntegerField()
    kind = models.ForeignKey(Kind, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Price(models.Model):
    name = models.IntegerField(unique=False)
    weight = models.OneToOneField(Weight, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Card(models.Model):
    name = models.CharField(max_length=64, blank=True, unique=False)
    kind = models.ForeignKey(Kind, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

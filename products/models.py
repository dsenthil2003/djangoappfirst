from django.db import models
from django.contrib.auth.models import User
DATE_INPUT_FORMATS = ['%d-%m-%Y']
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)


class Offer(models.Model):
    code = models.CharField(max_length=255)
    description = models.CharField(max_length=2018)
    discount = models.FloatField()


class Addtocart(models.Model):
    code = models.ForeignKey(Offer,on_delete=models.CASCADE)
    name = models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    dateoforder = models.DateField(null=True)





from django.db import models
#from django.contrib.auth.models import User
from common.models import User


# Create your models here.
class Sale(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.CharField(max_length=50)
    description = models.TextField()
    price = models.PositiveIntegerField()
    sold = models.BooleanField(default=False)
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.product


class Bid(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    content = models.TextField()
    agreed = models.BooleanField(default=False)
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)

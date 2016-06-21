from datetime import datetime

from django.contrib.auth.models import User
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Garage(models.Model):
    """
    Fields - Name, Address, Description, Open Times, Phone
    """
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    description = models.TextField(blank=True, null=True)
    openTime = models.TimeField()
    closeTime = models.TimeField()

    # manufacturers = models.ManyToManyField(
    #     Manufacturer,
    #     blank=True,
    # )

    def __str__(self):
        return "{} - {}".format(self.name, self.phone)

    def is_open(self):
        return self.openTime <= datetime.now().time() < self.closeTime


class Category(MPTTModel):
    """
    Fields - Name, Parent
    """

    name = models.CharField(max_length=30, unique=True)
    parent = TreeForeignKey("self", null=True, blank=True, related_name="children", db_index=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return "{} - {}".format(self.name, self.parent)
        # django-mptt


class Service(models.Model):
    """
    Fields - Name, Category, Price
    """

    name = models.CharField(max_length=30)
    category = models.ForeignKey(Category, null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=7)


class Customer(models.Model):
    user = models.OneToOneField(User, related_name='user')
    manufacturer = models.CharField(max_length=30)
    make = models.CharField(max_length=30)
    year = models.DateField()

    # class Manufacturer(models.Model):
    #     """
    #     Fields - Name, Country
    #     """
    #     name = models.CharField(max_length=30)
    #     country = models.CharField(max_length=30)
    #
    #     def __str__(self):
    #         return "{} - {}".format(self.name, self.country)


    #
    # class Make(models.Model):
    #     """
    #     Fields - Name, Country, Garage M2M
    #     """
    #     manufacturer = models.ForeignKey(
    #         Manufacturer,
    #         on_delete=models.CASCADE,
    #     )
    #     name = models.CharField(max_length=30)
    #     startYear = models.DateField()
    #     endYear = models.DateField()
    # # django-mptt
    # #

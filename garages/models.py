from django.db import models


# Create your models here.

# Garage Model:
class Garage(models.Model):
    """
    Fields - Name, Address, Description, Open Times, Phone
    """
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    description = models.TextField(blank=True, null=True)
    openTime = models.TimeField()
    closeTime = models.TimeField()

    def __str__(self):
        return "{} - {}".format(self.name, self.phone)



from django.db import models

# Create your models here.
# dealers/models.py
from django.db import models

class Dealer(models.Model):
    DealerId = models.AutoField(primary_key=True)
    number = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    firstName = models.CharField(max_length=100)

    def __str__(self):
        return self.name
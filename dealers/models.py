from django.db import models

class Dealer(models.Model):
    # Auto-generated unique identifier for the record
    id = models.AutoField(primary_key=True)
    # Event type (insert or update)
    event = models.CharField(max_length=50, default="testvalue")
    # User's full name
    name = models.CharField(max_length=255)
    # User's contact number
    number = models.CharField(max_length=50)
    # User's first name
    first_name = models.CharField(max_length=100)
    # User's last name
    last_name = models.CharField(max_length=100)
    # Status of the record, active or inactive
    status = models.CharField(max_length=20, choices=[('active', 'Active'), ('inactive', 'Inactive')], default="active")

    def __str__(self):
        return self.name

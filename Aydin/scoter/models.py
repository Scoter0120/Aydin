from django.db import models
import django.utils.timezone as timezone

class TD_DATA(models.Model):
    FACTORY = models.CharField(max_length=50)
    CATEGORY = models.CharField(max_length=50)
    VALUE = models.DecimalField(max_digits=8, decimal_places=2)
    DATA_DATE = models.CharField(max_length=50)
    UPDATE_TIME = models.DateTimeField(default=timezone.now)
    IP_ADDRESS = models.CharField(max_length=50)

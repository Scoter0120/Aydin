from django.db import models


class TD_DATA(models.Model):
    FACTORY = models.CharField(max_length=50)
    CATEGORY = models.CharField(max_length=50)
    VALUE = models.CharField(max_length=50)
    DATA_DATE = models.CharField(max_length=50)
    UPDATE_TIME = models.CharField(max_length=50)
    IP_ADDRESS = models.CharField(max_length=50)

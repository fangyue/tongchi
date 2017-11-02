# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone_number = models.CharField(max_length=50, blank=True)
    default_lat = models.FloatField(null=True, blank=True, default=0.0)
    default_lon = models.FloatField(null=True, blank=True, default=0.0)
    default_cafe = models.BigIntegerField(null=True, blank=True, default=0)
    default_interest = models.BigIntegerField(null=True, blank=True, default=0)

    class Meta(AbstractUser.Meta):
        pass

class Request(models.Model):
    user_id = models.IntegerField(blank=False, default=0)
    status = models.IntegerField(blank=False, default=0)
    lm_user_id = models.IntegerField(null=True, blank=True)
    matched_time = models.DateTimeField()
    request_start = models.DateTimeField()
    request_end = models.DateTimeField()
    request_lat = models.FloatField(null=True, blank=True, default=0.0)
    request_lon = models.FloatField(null=True, blank=True, default=0.0)
    request_cafe = models.BigIntegerField(null=True, blank=True, default=0)
    request_interest = models.BigIntegerField(null=True, blank=True, default=0)
    request_count = models.IntegerField(blank=False, default=0)
    # the number of lunchmate that a user would like to request
    lm_number = models.IntegerField(blank=False, default=1)

class History(models.Model):
    user_id = models.IntegerField(blank=False, default=0)
    lm_user_id = models.IntegerField(blank=False, default=0)
    rate = models.IntegerField(blank=False, default=0)
    review = models.CharField(max_length=200, blank=True)

# Create your models here.

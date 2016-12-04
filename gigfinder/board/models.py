"""
Models for the board app
"""
import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Application(models.Model):
    # event = models.ForeignKey(Event)
    user = models.ForeignKey(User)
    status = models.NullBooleanField(blank=True, default=None, null=True)

    def __str__(self):
        return self.user.username

class Event(models.Model):
    """
    Model for the one-time event postings
    """
    event_name = models.CharField(max_length=200)
    event_description_short = models.CharField(max_length=400, blank=True)
    event_description_long = models.CharField(max_length=2000)
    pub_date = models.DateTimeField(auto_now_add=True)
    event_date = models.DateField()
    event_time = models.TimeField(null=True)
    event_image = models.ImageField(null=True, blank=True)
    event_user = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    event_application = models.OneToOneField(Application, null=True)

    def __str__(self):
        return self.event_name


'''
class Job_Posting(models.Model):
    """
    Model for the regular job postings
    """
    posting_name = models.CharField(max_length=200)
    job_description_short = models.CharField(max_length=400, blank=True)
    job_description_long = models.CharField(max_length=2000)
    pub_date = models.DateTimeField(auto_now_add=True)
    start_date = models.DateField()
    end_date = models.DateField()
    pay = models.IntegerField(default=0)
    job_image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.posting_name
'''


class Musician_Advertisement(models.Model):
    """
    Model for the advertisements for availability by musicians
    """
    posting_name = models.CharField(null=True, max_length=200)
    musician_name = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    ad_description_short = models.CharField(max_length=400, blank=True)
    ad_description_long = models.CharField(max_length=2000)
    pub_date = models.DateTimeField(auto_now_add=True)
    start_availability = models.DateField()
    end_availability = models.DateField()
    ad_image = models.ImageField(null=True, blank=True)


    def __str__(self):
        return self.musician_name




from django.db import models
# Create your models here.


class ActivityPeriod(models.Model):
    start_time = models.DateField()
    end_time = models.DateField()    

    
class User(models.Model):
    id = models.CharField(max_length=64,primary_key=True)
    real_name = models.CharField(max_length=64)
    tz = models.CharField(max_length=64)
    activity_periods = models.ManyToManyField(ActivityPeriod)


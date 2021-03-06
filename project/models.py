import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Mytable(models.Model):
    time = models.DateTimeField(auto_now_add=True) # when the record is created 
                                                   # then automatically save the time.
    tmp = models.CharField(max_length = 10) # save the current temp
    stat = models.CharField(max_length = 10) # 0 : Off, 1 :On
    strength = models.CharField(max_length = 10,default = "Not")
    def __str__(self):
        return self.tmp

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


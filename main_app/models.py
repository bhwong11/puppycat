from django.db import models
import uuid
# Create your models here.


class Vacation(models.Model):
    vacation_id = models.AutoField(primary_key=True)
    place = models.CharField(max_length=100)
    days_off = models.IntegerField()
    cool = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.place

    class Meta:
        ordering = ['days_off']


class Activities(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    vacation = models.ForeignKey(Vacation, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

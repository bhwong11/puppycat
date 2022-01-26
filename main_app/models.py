from django.db import models

# Create your models here.

class Vacation(models.Model):
    place = models.CharField(max_length=100)
    days_off = models.IntegerField()
    cool = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.place

    class Meta:
        ordering = ['days_off']

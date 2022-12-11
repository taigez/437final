from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=200)
    xpos = models.IntegerField(default=0)
    ypos = models.IntegerField(default=0)
    in_date = models.DateTimeField(editable=False)
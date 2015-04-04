from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Mood(models.Model):
    user = models.ForeignKey(User)
    time = models.DateTimeField()
    angry = models.DecimalField(max_digits=7, decimal_places=6)
    sad = models.DecimalField(max_digits=7, decimal_places=6)
    surprised = models.DecimalField(max_digits=7, decimal_places=6)
    happy = models.DecimalField(max_digits=7, decimal_places=6)

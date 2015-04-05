from django.db import models
from django.contrib.auth.models import User
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

# Create your models here.
class Mood(models.Model):
    user = models.ForeignKey(User)
    time = models.DateTimeField()
    angry = models.FloatField()
    sad = models.FloatField()
    surprised = models.FloatField()
    happy = models.FloatField()

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Positivo(models.Model):
    email = models.EmailField()
    temp = models.DecimalField(default=36.5, max_digits=3, decimal_places=1, validators=[MinValueValidator(25), MaxValueValidator(50)])
    oxi = models.DecimalField(default=93, max_digits=3, decimal_places=0, validators=[MinValueValidator(60), MaxValueValidator(100)])
    timestamp = models.DateTimeField(auto_now_add = True)
    vali = models.BooleanField(default=False)
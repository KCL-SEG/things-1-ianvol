from django.db import models

class Thing(models.Model):
    name = models.CharField(max_length=255, unique = True)
    description = models.TextField(max_length=120, blank=True)
    quantity = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
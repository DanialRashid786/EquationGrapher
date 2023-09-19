from django.db import models
import numpy as np

# Create your models here.
class Equation(models.Model):
    expression = models.CharField(max_length=100)  # Assuming equation strings won't exceed 100 characters
    x_min = models.FloatField()
    x_max = models.FloatField()

    def __str__(self):
        return self.expression



# Uncomment the following imports before adding the Model code

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # Other fields as needed

    def __str__(self):
        return self.name  # Return the name as the string representation


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
class CarModel(models.Model):
    car_make = models.ForeignKey(
        CarMake, on_delete=models.CASCADE)  # Many-to-One relationship
    name = models.CharField(max_length=100)
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('MYVI', 'Myvi'),
        ('DB9', 'Db9'),
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')
    year = models.IntegerField(
        default=2023,
        validators=[
                    MaxValueValidator(2023),
                    MinValueValidator(2015)])
    color = models.CharField(max_length=10)
    # Other fields as needed

    def __str__(self):
        return self.name  # Return the name as the string representation

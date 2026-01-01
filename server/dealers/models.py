from django.db import models

class Dealer(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'dealers'

class CarMake(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'car_makes'

class CarModel(models.Model):
    make = models.ForeignKey(CarMake, on_delete=models.CASCADE, related_name='models')
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.make.name} {self.name}"

    class Meta:
        db_table = 'car_models'
        unique_together = ['make', 'name']

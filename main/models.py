from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name
    
    def __repr__(self):
        return f"Pk: {self.pk}, brand: {self.name}"


class Car(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='cars')
    name = models.CharField(max_length=150)
    color = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    type = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Pk: {self.pk}, car: {self.name}"
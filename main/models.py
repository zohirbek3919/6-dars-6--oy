from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name
    
    def __repr__(self):
        return f"Pk: {self.pk}, brand: {self.name}"


class Car(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    text = models.CharField(max_length=150)
    color = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Pk: {self.pk}, car: {self.name}"
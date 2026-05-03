from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Pk: {self.pk}, category: {self.name}"


class New(models.Model):
    turi = models.ForeignKey(Category, on_delete=models.CASCADE)
    type = models.CharField(max_length=150)
    name = models.CharField(max_length=150)
    text = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Pk: {self.pk}, new: {self.name}"
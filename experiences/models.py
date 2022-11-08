from django.db import models


class Experience(models.Model):
    type = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField()
    duration = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

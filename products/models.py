from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=255)
    friendly_name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Wine(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField()
    grape_variety = models.CharField(max_length=255, null=True, blank=True)
    vintage = models.CharField(max_length=255, null=True, blank=True)
    certification = models.CharField(max_length=255, null=True, blank=True)
    colour = models.CharField(max_length=255, null=True, blank=True)
    type = models.CharField(max_length=255, null=True, blank=True)
    alcohol_content = models.CharField(max_length=255, null=True, blank=True)
    format = models.CharField(max_length=255, null=True, blank=True)
    place_of_origin = models.CharField(max_length=255, null=True, blank=True)
    vegan_ok = models.ImageField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=False)

    def __str__(self):
        return self.name


class Food(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    type = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField()
    ingredients = models.CharField(max_length=255, null=True, blank=True)
    certification = models.CharField(max_length=255, null=True, blank=True)
    format = models.CharField(max_length=255, null=True, blank=True)
    place_of_origin = models.CharField(max_length=255, null=True, blank=True)
    vegan_ok = models.ImageField(null=True, blank=True)
    shelf_life = models.CharField(max_length=255, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name


class ExperienceType(models.Model):

    class Meta:
        verbose_name = 'Experience Type'

    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    type = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField()
    duration = models.CharField(max_length=255, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

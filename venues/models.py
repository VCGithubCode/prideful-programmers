from django.db import models

CATEGORY = [
    ('Café', 'Café'),
    ('Club', 'Club'),
    ('Support Center', 'Support Center'),
]

class City(models.Model):
    city_name = models.CharField(max_length=100, unique=True, null=False, blank=False)
    country = models.CharField(max_length=100, unique=True, null=False, blank=False)

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'
        
    def __str__(self):
        return self.city_name

class Venue(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False, blank=False)
    address = models.TextField(max_length=500, null=False, blank=False)
    contact_info = models.CharField(max_length=200, null=False, blank=False)
    opening_hours = models.TextField(max_length=200, null=False, blank=False)
    special_features = models.CharField(max_length=200)
    category = models.CharField(
        choices=CATEGORY, max_length=50, null=False, blank=False)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
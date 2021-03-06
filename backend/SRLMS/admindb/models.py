from django.db import models
from django.conf import settings
# from authentication.models import User

# class Metadata(models.Model):
#     admin = models.OneToOneField(User, on_delete=models.CASCADE)
#     spam_block_days = models.IntegerField(default=10)
#     alert_level = models.IntegerField(default=20)

class Location(models.Model):
    official = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='locations')
    area = models.FloatField(default=0)
    budget_alloc = models.BigIntegerField(default=10000)
    under_construction = models.BooleanField(default=True)
    def __str__(self):
        return '{0}: Location'.format(self.official)

class Marker(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='markers')
    x = models.FloatField(default=0)
    y = models.FloatField(default=0)

    def __str__(self):
        return '{0}: Marker'.format(self.location)

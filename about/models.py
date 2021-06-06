from django.db import models


class About(models.Model):
    description = models.TextField(blank=True, null=True)
    vision = models.CharField(max_length=300, blank=True, null=True)
    mission = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.description

from django.db import models

class Coffee(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    image = models.CharField(max_length=2083)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name
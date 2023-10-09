from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField ( max_length = 100)
    brand = models.CharField (max_length=100)
    count = models.PositiveBigIntegerField()
    description = models.TextField(max_length=200, default='Базовое описание') 

    def __repr__(self) :
        return f"Item({self.name},{self.brand},{self.count}"
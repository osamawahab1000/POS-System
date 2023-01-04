from django.db import models

# Create your models here.
class Product(models.Model):
    name_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    name_Description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='POS_System/images/')
    price = models.FloatField(default=0)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.name

from django.db import models

# Create your models here.
class Payment(models.Model):
    source = models.CharField(max_length=200)
    begin_date = models.DateField()
    end_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.source

class Income(models.Model):
    source = models.CharField(max_length=200)
    begin_date = models.DateField()
    end_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.source

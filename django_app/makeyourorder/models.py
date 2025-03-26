from django.db import models

# Create your models here.
class Makeyourorder(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    phone = models.CharField(max_length=150)
    message = models.TextField(blank=True , null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
            return f'{self.name} - {self.email} - {self.phone} - {self.message} - {self.date}'


from django.db import models

class Contact_info(models.Model):
    name = models.CharField(max_length=100, null=False)
    mobile_number = models.CharField(max_length=20, null=True)
    country = models.CharField(max_length=100, null= False)
    city = models.CharField(max_length=100, null= True)

    def __str__(self):
        return self.name

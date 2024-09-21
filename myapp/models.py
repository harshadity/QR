from django.db import models
from django.contrib.auth import get_user_model

class Company(models.Model):
    name = models.CharField(max_length=255)
    number_of_outlets = models.IntegerField()
    number_of_employees = models.IntegerField()
    address = models.TextField()
    gts_number = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Outlet(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='outlets')
    logo = models.ImageField(upload_to='logos/')
    gst_number = models.CharField(max_length=50)
    name = models.CharField(max_length=255)
    account_details = models.TextField()
    outlet_name = models.CharField(max_length=255)
    address = models.TextField()

    def __str__(self):
        return self.outlet_name

class OutletAccess(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    outlet = models.ForeignKey(Outlet, on_delete=models.CASCADE)
    permissions = models.JSONField()

    def __str__(self):
        return f'{self.user} - {self.outlet}'

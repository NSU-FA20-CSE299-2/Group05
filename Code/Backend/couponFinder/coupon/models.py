from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)


    def __str__(self):
        return self.name

class Coupon(models.Model):
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=500, null=True)
    code = models.CharField(max_length=200, null=True)
    image= models.ImageField(null = True, blank= True)


    def __str__(self):
        return self.name


    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Gadget_coupon(models.Model):
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=500, null=True)
    code = models.CharField(max_length=200, null=True)
    image= models.ImageField(null = True, blank= True)


    def __str__(self):
        return self.name


    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Fashion_coupon(models.Model):
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=500, null=True)
    code = models.CharField(max_length=200, null=True)
    image= models.ImageField(null = True, blank= True)


    def __str__(self):
        return self.name


    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
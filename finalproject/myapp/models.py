from django.db import models


class Home(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=50)
    image = models.FileField(blank=True, upload_to='blog_images')

class AdminUser(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    title = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=50, null=True)
    Address = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=50, null=True)
    zip = models.CharField(max_length=50, null=True)
    image = models.FileField(blank=True, upload_to='blog_images')
    terms_confirmed = models.BooleanField(default=True)


class AddProperty(models.Model):
    adminuser = models.ForeignKey(AdminUser, on_delete=models.CASCADE, null=True)
    mlsnumber = models.CharField(max_length=50)
    listingprice = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    streetaddress1 = models.CharField(max_length=50, null=True)
    streetaddress2 = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=50, null=True)
    country = models.CharField(max_length=50, null=True)
    postalcode = models.CharField(max_length=50, null=True)
    createdby = models.CharField(max_length=50, null=True)
    image = models.FileField(blank=True, upload_to='blog_images')


class PageContent1(models.Model):
    title = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    content = models.CharField(max_length=50)
    image = models.FileField(blank=True, upload_to='blog_images')


class AboutUs(models.Model):
    title = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    content = models.CharField(max_length=50)
    image = models.FileField(blank=True, upload_to='blog_images')
    img = models.FileField(blank=True, upload_to='blog_images')


class Faq(models.Model):
    question = models.CharField(max_length=50)
    answer = models.CharField(max_length=50)


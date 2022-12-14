from django.db import models
from django.urls import reverse
from .helper import *


# Create your models here.


class GeneralSettings(models.Model):
    logo = models.FileField(upload_to="General Settings")

    instagram = models.CharField(max_length=200, null=True, blank=True)
    facebook = models.CharField(max_length=200, null=True, blank=True)
    youtube = models.CharField(max_length=200, null=True, blank=True)
    twitter = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return "General Settings"
    

    class Meta:
        verbose_name_plural = "General Settings"


class Index_First_Slider(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="Index_First")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Index First Slider"
        verbose_name_plural = "Index First Silders"

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"
    


class Work(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True)
    client = models.CharField(max_length=100,null=True)
    location = models.CharField(max_length=150,null=True)
    date = models.DateField(null=True)
    image = models.ImageField(upload_to="Work")
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name="work",null=True)
    slug = models.SlugField(editable=False, null=True)
    

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(Work, self).save(*args, **kwargs)
        self.slug = seo(self.name)
        super(Work, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('portfolio_details', kwargs={"slug": self.slug})


class Images(models.Model):
    image = models.ImageField(upload_to="Main_Images")
    work = models.ForeignKey(Work, on_delete=models.CASCADE,related_name="images",null=True)
    


    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"


class Index_Settings(models.Model):
    main_image = models.FileField(upload_to="Main Index")
    name_part = models.CharField(max_length=50, null=True)
    profession = models.CharField(max_length=50, null=True)
    # who am i
    text_1 = models.TextField(null=True)
    image_1 = models.ImageField(upload_to="Who am I", null=True)
    image_2 = models.ImageField(upload_to="Who am I", null=True)
    image_3 = models.ImageField(upload_to="Who am I", null=True)
    text_2 = models.TextField(null=True)
    # what we do
    description = models.TextField(null=True)

    class Meta:
        verbose_name = "Index Settings"
        verbose_name_plural = "Index Settings"


class Services(models.Model):
    name = models.CharField(max_length=50)
    logo = models.FileField(upload_to="Services")
    about = models.TextField(null=True)
    slug = models.SlugField(editable=False, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"

    def save(self, *args, **kwargs):
        super(Services, self).save(*args, **kwargs)
        self.slug = seo(self.name)
        super(Services, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('service_detail', kwargs={"slug": self.slug})


class Service_Images(models.Model):
    image = models.ImageField(upload_to="Images")
    service = models.ForeignKey(
        Services, on_delete=models.CASCADE, related_name="images")
    created_date = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name = "Service Image"
        verbose_name_plural = "Service Images"


class Offers(models.Model):
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField()

    class Meta:
        verbose_name = "Offer"
        verbose_name_plural = "Offers"


class Options(models.Model):
    option = models.CharField(max_length=150)
    offer = models.ForeignKey(
        Offers, on_delete=models.CASCADE, related_name="options")

    class Meta:
        verbose_name = "Option"
        verbose_name_plural = "Options"


class Booking(models.Model):
    name = models.CharField(max_length=50)
    number = models.CharField(max_length=20)
    email = models.EmailField()
    book_date = models.CharField(max_length=150)
    message = models.TextField()
    service = models.CharField(max_length=50,null=True,blank=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Booking"


class Why_Us_Detail(models.Model):
    title = models.CharField(max_length=50)
    about = models.TextField()

    class Meta:
        verbose_name = "Why Choose us in detail"
        verbose_name_plural = "Why Choose us in detail"


class Why_Options(models.Model):
    option = models.CharField(max_length=100)
    why = models.ForeignKey(
        Why_Us_Detail, on_delete=models.CASCADE, related_name="options")

    class Meta:
        verbose_name = "Why Us Options"
        verbose_name_plural = "Why Us Options"


class About(models.Model):
    title = models.TextField()
    description = models.TextField()
    image_right = models.ImageField(upload_to="Image Right About",null=True)

    class Meta:
        verbose_name_plural = "About"


class Member(models.Model):
    name = models.CharField(max_length=30)
    position = models.CharField(max_length=50)
    image = models.ImageField(upload_to="Team Member")
    #social
    instagram = models.CharField(max_length=200,null=True,blank=True)
    facebook = models.CharField(max_length=200, null=True, blank=True)
    youtube = models.CharField(max_length=200,null=True,blank=True)
    twitter = models.CharField(max_length=200, null=True, blank=True)


    def __str__(self):
        return self.name
    
    

class AboutSliderImage(models.Model):
    image = models.ImageField(upload_to="About Slider Images")
    about = models.ForeignKey(About, on_delete=models.CASCADE,related_name="images")


class Contact(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=200)
    number = models.CharField(max_length=150)
    email = models.EmailField()

    location_src = models.TextField()

    def __str__(self):
        return "Contact"

    class Meta:
        verbose_name_plural = "Contact"

class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name

    



    

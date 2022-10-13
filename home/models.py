
from calendar import c
from email.policy import default
from re import A
import uuid 
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    username = models.CharField(max_length=100, null=False, blank=True)
    email = models.EmailField(unique=True, null=True)
    
    Country = models.CharField(max_length=100, null=False, blank=True)
    Address = models.CharField(max_length=100, null=False, blank=True)
    phonenumber = models.CharField(max_length=100, null=False, blank=True)
    
    is_staff= models.BooleanField(default=False)
    is_active= models.BooleanField(default=True)
    
    avatar = models.ImageField(null=True, default="avatar.svg")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name']

class Topic(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Color(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class Jewelry(models.Model):
    
    views = models.IntegerField(default=0)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable= False)
    
    topics = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    color = models.ManyToManyField(Color)
    tag = models.ManyToManyField(Tag)
    
    name = models.CharField(max_length=80)
    description = models.TextField(null=True, blank=True)

    imagemain = models.ImageField(upload_to="Jewelry_banners/", default="static/images/icons/user.svg", blank=False)
    image2 = models.ImageField(upload_to="Jewelry_banners/", default="static/images/icons/user.svg", blank=True)
    image3 = models.ImageField(upload_to="Jewelry_banners", default="static/images/icons/user.svg", blank=True)
    image4 = models.ImageField(upload_to="Jewelry_banners", default="static/images/icons/user.svg", blank=True)
    image5 = models.ImageField(upload_to="Jewelry_banners", default="static/images/icons/user.svg", blank=True)
    image6 = models.ImageField(upload_to="Jewelry_banners", default="static/images/icons/user.svg", blank=True)
    
    
    
    price = models.IntegerField(default=0)
    newcoming = models.BooleanField(default=True)
    
    updated = models.DateTimeField(auto_now=True)
    created = models.DateField(auto_now_add=True)
    
    class Meta:
        ordering = ['-updated', '-created']
    
    def __str__(self):
        return self.name
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    Jewelry = models.ForeignKey(Jewelry, on_delete=models.CASCADE)
    body = models.TextField(blank=False)
    
    Reviews = ((1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5'))
    review = models.IntegerField(default=5, choices=Reviews)
    
    updated = models.DateTimeField(auto_now=True)
    created = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.body[0:50]
 
class CartItem(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable= True)
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    Jewelry = models.ForeignKey(Jewelry, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    totalprice = models.IntegerField(default=0)

class Order(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable= False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)     
    ordernumber = models.IntegerField(default=0, blank=False)
    
    FirstName = models.CharField(max_length=100, null=False, blank=False)
    SecondName = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(unique=False, null=True)
    
    Address = models.CharField(max_length=100, null=False, blank=False)
    Country = models.CharField(max_length=100, null=False, blank=False)
    Zip = models.IntegerField(default=0, blank=False)
        
    phonenumber = models.CharField(max_length=100, null=False, blank=False)
    
    ordered_items = models.ManyToManyField(Jewelry)
    shippingstatus =  models.BooleanField(default=False)
    
    def __int__(self):
        return self.ordernumber
    
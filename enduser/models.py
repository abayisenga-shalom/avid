
from django.db import models
from django.db.models.fields import CharField
import uuid
import random

# Create your models here.

class Agent(models.Model):
    name = models.CharField(max_length=50)
    agent_photo = models.ImageField(upload_to='agent_profile/')

    class Meta:
        verbose_name_plural='Agents'

    def __str__(self):
        return self.name

class House(models.Model):
    title = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    price = models.CharField(max_length=100)
    area = models.CharField(max_length=20)
    beds = models.CharField(max_length=20)
    baths = models.CharField(max_length=20)
    garage = models.CharField(max_length=20)
    description = models.CharField(max_length=1000)
    image1 = models.ImageField(upload_to='properties/apartments/')
    image2 = models.ImageField(upload_to='properties/apartments/')
    image3 = models.ImageField(upload_to='properties/apartments/')
    image4 = models.ImageField(upload_to='properties/apartments/')
    image5 = models.ImageField(upload_to='properties/apartments/', blank=True)
    image6 = models.ImageField(upload_to='properties/apartments/', blank=True)
    image8 = models.ImageField(upload_to='properties/apartments/', blank=True)
    image9 = models.ImageField(upload_to='properties/apartments/', blank=True)
    image10 = models.ImageField(upload_to='properties/apartments/', blank=True)
    image11 = models.ImageField(upload_to='properties/apartments/', blank=True)
    image12 = models.ImageField(upload_to='properties/apartments/', blank=True)
    video_Url= models.CharField(max_length=500, blank=True)
    agent = models.ForeignKey(Agent,on_delete=models.CASCADE)
    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural='Houses'

    def __str__(self):
        return self.title


class Commerce(models.Model):

    title = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    price = models.CharField(max_length=100)
    area = models.CharField(max_length=20)
    description = models.CharField(max_length=1000)
    image1 = models.ImageField(upload_to='properties/commerces/')
    image2 = models.ImageField(upload_to='properties/commerces/')
    image3 = models.ImageField(upload_to='properties/commerces/')
    image4 = models.ImageField(upload_to='properties/commerces/')
    image5 = models.ImageField(upload_to='properties/commerces/', blank=True)
    image6 = models.ImageField(upload_to='properties/commerces/', blank=True)
    image8 = models.ImageField(upload_to='properties/commerces/', blank=True)
    image9 = models.ImageField(upload_to='properties/commerces/', blank=True)
    image10 = models.ImageField(upload_to='properties/commerces/', blank=True)
    image11 = models.ImageField(upload_to='properties/commerces/', blank=True)
    image12 = models.ImageField(upload_to='properties/commerces/', blank=True)
    video_Url= models.CharField(max_length=500, blank=True)
    agent = models.ForeignKey(Agent,on_delete=models.CASCADE)
    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural='Commerces'

    def __str__(self):
        return self.name


class Apartment(models.Model):

    title = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    price = models.CharField(max_length=100)
    area = models.CharField(max_length=20)
    beds = models.CharField(max_length=20)
    baths = models.CharField(max_length=20)
    garage = models.CharField(max_length=20)
    description = models.CharField(max_length=1000)
    image1 = models.ImageField(upload_to='properties/apartments/')
    image2 = models.ImageField(upload_to='properties/apartments/')
    image3 = models.ImageField(upload_to='properties/apartments/')
    image4 = models.ImageField(upload_to='properties/apartments/')
    image5 = models.ImageField(upload_to='properties/apartments/', blank=True)
    image6 = models.ImageField(upload_to='properties/apartments/', blank=True)
    image8 = models.ImageField(upload_to='properties/apartments/', blank=True)
    image9 = models.ImageField(upload_to='properties/apartments/', blank=True)
    image10 = models.ImageField(upload_to='properties/apartments/', blank=True)
    image11 = models.ImageField(upload_to='properties/apartments/', blank=True)
    image12 = models.ImageField(upload_to='properties/apartments/', blank=True)
    video_Url= models.CharField(max_length=500, blank=True)
    agent = models.ForeignKey(Agent,on_delete=models.CASCADE)
    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural='Apartments'

    def __str__(self):
        return self.name


class Room(models.Model):

    title = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    price = models.CharField(max_length=100)
    area = models.CharField(max_length=20)
    beds = models.CharField(max_length=20)
    baths = models.CharField(max_length=20)
    description = models.CharField(max_length=1000)
    image1 = models.ImageField(upload_to='properties/rooms/')
    image2 = models.ImageField(upload_to='properties/rooms/')
    image3 = models.ImageField(upload_to='properties/rooms/')
    image4 = models.ImageField(upload_to='properties/rooms/')
    image5 = models.ImageField(upload_to='properties/rooms/', blank=True)
    image6 = models.ImageField(upload_to='properties/rooms/', blank=True)
    image8 = models.ImageField(upload_to='properties/rooms/', blank=True)
    image9 = models.ImageField(upload_to='properties/rooms/', blank=True)
    image10 = models.ImageField(upload_to='properties/rooms/', blank=True)
    image11 = models.ImageField(upload_to='properties/rooms/', blank=True)
    image12 = models.ImageField(upload_to='properties/rooms/', blank=True)
    video_Url= models.CharField(max_length=500, blank=True)
    agent = models.ForeignKey(Agent,on_delete=models.CASCADE)
    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural='Rooms'

    def __str__(self):
        return self.name


class Land(models.Model):

    title = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    price = models.CharField(max_length=100)
    area = models.CharField(max_length=20)
    description = models.CharField(max_length=1000)
    image1 = models.ImageField(upload_to='properties/lands/')
    image2 = models.ImageField(upload_to='properties/lands/')
    image3 = models.ImageField(upload_to='properties/lands/')
    image4 = models.ImageField(upload_to='properties/lands/')
    image5 = models.ImageField(upload_to='properties/lands/', blank=True)
    image6 = models.ImageField(upload_to='properties/lands/', blank=True)
    image8 = models.ImageField(upload_to='properties/lands/', blank=True)
    image9 = models.ImageField(upload_to='properties/lands/', blank=True)
    image10 = models.ImageField(upload_to='properties/lands/', blank=True)
    image11 = models.ImageField(upload_to='properties/lands/', blank=True)
    image12 = models.ImageField(upload_to='properties/lands/', blank=True)
    video_Url= models.CharField(max_length=500, blank=True)
    agent = models.ForeignKey(Agent,on_delete=models.CASCADE)
    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural='Lands'

    def __str__(self):
        return self.name


class Vehicle(models.Model):

    title = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    price = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    image1 = models.ImageField(upload_to='properties/vehicles/')
    image2 = models.ImageField(upload_to='properties/vehicles/')
    image3 = models.ImageField(upload_to='properties/vehicles/')
    image4 = models.ImageField(upload_to='properties/vehicles/')
    image5 = models.ImageField(upload_to='properties/vehicles/', blank=True)
    image6 = models.ImageField(upload_to='properties/vehicles/', blank=True)
    image8 = models.ImageField(upload_to='properties/vehicles/', blank=True)
    image9 = models.ImageField(upload_to='properties/vehicles/', blank=True)
    image10 = models.ImageField(upload_to='properties/vehicles/', blank=True)
    image11 = models.ImageField(upload_to='properties/vehicles/', blank=True)
    image12 = models.ImageField(upload_to='properties/vehicles/', blank=True)
    video_Url= models.CharField(max_length=500, blank=True)
    agent = models.ForeignKey(Agent,on_delete=models.CASCADE)
    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural='Vehicles'

    def __str__(self):
        return self.name


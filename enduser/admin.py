from django.contrib import admin
from .models import Agent, Apartment, Commerce, Land, Room, Vehicle
from .models import House

# Register your models here.


admin.site.register(Agent)
admin.site.register(House)
admin.site.register(Apartment)
admin.site.register(Land)
admin.site.register(Vehicle)
admin.site.register(Room)
admin.site.register(Commerce)

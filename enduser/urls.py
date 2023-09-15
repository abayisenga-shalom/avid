from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('property-apartment', views.apartment),
    path('property-room', views.room),
    path('property-commerce', views.commerce),
    path('property-house', views.house),
    path('property-land', views.land),
    path('property-vehicle', views.vehicle),
    path('property-single', views.single),
    path('contact-us', views.contact),
    path('get-job', views.get_job),
    path('history', views.history),
    path('team', views.team),
    path('blog', views.blog)
]
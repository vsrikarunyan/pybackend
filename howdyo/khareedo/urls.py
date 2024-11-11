from django.urls import path

from . import views

urlpatterns = [
    path('howdy/<str:name>', 
         views.howdy, 
         name='howdy'),
    path('howdy/',
         views.howdy,
         name='howdy_default'),
]
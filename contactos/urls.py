from django.urls import path , include
from .views import Contacto

urlpatterns = [

      path('', Contacto, name="contacto"),    

    
]
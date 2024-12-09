from django.contrib import admin


from .models import Contacto

class ContactoAdmin(admin.ModelAdmin):
    model=Contacto
    list_display=['nombres' , 'apellidos' , 'celular' ,'correo' , 'tipo_consulta' , 'mensaje']
    

admin.site.register(Contacto)
# Register your models here.

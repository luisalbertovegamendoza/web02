from django import forms
from .models import Contacto

class ContactoForm(forms.ModelForm):
    class Meta:
        model=Contacto
        fields=['nombres' ,'apellidos' , 'celular' ,'correo' , 'tipo_consulta' , 'mensaje' , 'avisos']



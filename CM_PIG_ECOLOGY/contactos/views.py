from django.shortcuts import render

from django.views.generic import TemplateView

from .forms import ContactoForm


def Contacto(request):
    data={
        'form' : ContactoForm()
    }

    if request.method =='POST':
        formulario=ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "contacto guardado"
        else:
            data["form"] =formulario

    return render (request, "contactos/contactos.html",data)
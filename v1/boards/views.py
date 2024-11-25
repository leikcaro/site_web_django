from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class IndexPageView(TemplateView): #clase que nos permite renderizar una pagina sencilla sin lógica
    template_name = "index.html"
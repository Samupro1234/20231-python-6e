
from django.template import Context, Template, loader
from django.http import HttpResponse
from blog.models import usuario

rutaTemplates = "D:/6KHIPU/LENGUAJE DE PROGRAMACION PYTHON/django/myproyecto4/plantilla"
                
#def home(response):
#    doc = open( rutaTemplates + "/home.html" )
#    plant = Template( doc.read() )
#    doc.close()
#    datos = {"nombre": "Vladimir"}
#    contexto = Context(datos)
#    salida = plant.render(contexto)
#    return HttpResponse(salida)

def contacto(response):
    doc = loader.get_template( "contacto.html" )
    print(rutaTemplates)
    salida = doc.render()
    return HttpResponse(salida)

def portafolio(response):
    doc = loader.get_template( "portafolio.html")
    return HttpResponse(doc.render())

def productos(response):
    return HttpResponse(loader.get_template("productos.html").render())

def home(response):
    
    return HttpResponse(loader.get_template( "home.html" ).render())

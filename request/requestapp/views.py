from django.http import HttpResponse, JsonResponse, StreamingHttpResponse, FileResponse, HttpResponseBase, Http404

from django.shortcuts import render
from django.template import loader
import os
from django.conf import settings
import time

def index(request):
    return render(request, "requestapp/index.html")

def request_page(request):
    nombre = ""

    if request.method == 'POST':
        nombre = request.POST.get('nombre', '')

    return render(request, 'requestapp/request_page.html', {'nombre': nombre})

def app_attibutes(request):
    request.atributo =  'atributo seteado en la vista'
    return render(request,'requestapp/request_app_attributes.html',  {'atributo': request.atributo})


def middleware_view(request):
    value = getattr(request, 'custom_attribute', 'No se encontró el atributo')
    return JsonResponse({'middleware_attribute': value})

def querydict_view(request):
    return JsonResponse({'querydict': dict(request.GET)})

def json_response(request):
    return JsonResponse({'mensaje': 'Respuesta en formato JSON'})


def is_secure(request):
    return render(request, 'requestapp/is_secure.html', {'seguro': request.is_secure()})

def home(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre', 'Desconocido')
        return HttpResponse(f"¡Hola, {nombre}! Recibimos tu formulario con POST.")
    return render(request, 'requestapp/home.html')

def response(request):
    template = loader.get_template('requestapp/response.html')
    contexto = {'response': 'utilizando HTTPRESPONSE'}
    html = template.render(contexto, request)
    return HttpResponse(html)

def response_subclasses(request):
    response = HttpResponse("<h1>Esta es una respuesta con encabezados personalizados</h1>", content_type="text/html")

    response['X-App-Developer'] = 'TuNombre'
    response['X-Example-Header'] = 'Este es un encabezado extra'
    response['Cache-Control'] = 'no-cache'

    return response

def streaming_response(request):
    if request.GET.get("stream") == "1":
        def generador():
            yield "Inicio streaming...\n"
            time.sleep(1)
            yield "Mitad streaming...\n"
            time.sleep(1)
            yield "Fin streaming...\n"
        return StreamingHttpResponse(generador(), content_type='text/plane')
    
    return render(request, 'requestapp/response_streaming.html')


def file_response(request):
    file_path = os.path.join(settings.BASE_DIR, 'requestapp', 'archivos', 'archivo.pdf')
    return FileResponse(open(file_path, 'rb'), content_type='application/pdf')

def response_base(request):
    template = loader.get_template('requestapp/response_base.html')
    rendered_html = template.render({}, request)

    class CustomResponse(HttpResponseBase):
        def __init__(self, content, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self._content = content.encode('utf-8')
            self['Content-Type'] = 'text/html'
            self.streaming = False

        def getvalue(self):
            return self._content

        def __iter__(self):
            yield self._content

        @property
        def content(self):
            return self._content

        @content.setter
        def content(self, value):
            self._content = value

    return CustomResponse(rendered_html)
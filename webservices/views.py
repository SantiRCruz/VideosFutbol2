from home.models import *
from .serializer import * 
from rest_framework import viewsets

# Create your views here.

class video_viewset(viewsets.ModelViewSet):
    queryset =  Video.objects.all()
    serializer_class = Video_serializer

class equipo_viewset(viewsets.ModelViewSet):
    queryset =  Equipo.objects.all()
    serializer_class = Equipo_serializer

class jugador_viewset(viewsets.ModelViewSet):
    queryset =  Jugador.objects.all()
    serializer_class = Jugador_serializer    

class categoria_viewset(viewsets.ModelViewSet):
    queryset =  Categoria.objects.all()
    serializer_class = Categoria_serializer   
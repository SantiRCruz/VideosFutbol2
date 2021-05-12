from rest_framework import serializers
from home.models import *

class Video_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =  Video
        fields = ('url','nombreVideo','descripcion','videoArchivo','fechaPublicacion','Jugador','Equipo','categoria') 

class Equipo_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =  Equipo
        fields = ('url','nombreEquipo','Escudo',) 

class Jugador_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =  Jugador
        fields = ('url','nombre','foto')                 

class Categoria_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =  Categoria
        fields = ('url','tipoCategoria',)            
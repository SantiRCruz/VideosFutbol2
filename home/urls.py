from django.urls import path
from .views import *
urlpatterns = [
    path('',inicio_view, name = 'inicio_view'),
    path('about/',about_view, name ='about_view'),
    path('contacto/',contacto_view, name='contacto_view'),
    path('videos/',listar_videos_view, name = 'listar_videos_view'),
    path('equipos/',listar_equipos_view, name= 'listar_equipos_view'),
    path('jugadores/',listar_jugadores_view, name='listar_jugadores_view'),
    path('categorias/',listar_categorias_view, name = 'listar_categorias_view'),


    path('agregar_video/',agregar_video_view, name = 'agregar_video'),
    path('agregar_equipo/',agregar_equipo_view, name= 'agregar_equipo'),
    path('agregar_jugador/',agregar_jugador_view, name='agregar_jugador'),
    path('agregar_categoria/',agregar_categoria_view, name = 'agregar_categoria'),


    path('ver_video/<int:id_video>',ver_video_view, name = 'ver_video_view'),
    path('eliminar_video/<int:id_video>',eliminar_video_view, name = 'eliminar_video_view'),
    path('editar_video/<int:id_video>',editar_video_view, name = 'editar_video_view'),

    path('ver_equipo/<int:id_equipo>',ver_equipo_view, name = 'ver_equipo_view'),
    path('eliminar_equipo/<int:id_equipo>',eliminar_equipo_view, name = 'eliminar_equipo_view'),
    path('editar_equipo/<int:id_equipo>',editar_equipo_view, name = 'editar_equipo_view'),

    path('ver_jugador/<int:id_jugador>',ver_jugador_view, name = 'ver_jugador_view'),
    path('eliminar_jugador/<int:id_jugador>',eliminar_jugador_view, name = 'eliminar_jugador_view'),
    path('editar_jugador/<int:id_jugador>',editar_jugador_view, name = 'editar_jugador_view'),

    path('ver_categoria/<int:id_categoria>',ver_categoria_view, name = 'ver_categoria_view'),
    path('eliminar_categoria/<int:id_categoria>',eliminar_categoria_view, name = 'eliminar_categoria_view'),
    path('editar_categoria/<int:id_categoria>',editar_categoria_view, name = 'editar_categoria_view'),

    path('login/',login_view, name = 'login_view'),
    path('logout/',logout_view, name = 'logout_view'),

    path('register/',register_view,name='register_view'),
]
   


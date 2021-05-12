from django.urls import path, include
from rest_framework import routers
from home.models import *
from webservices.views import *

router =  routers.DefaultRouter()
router.register(r'videos',video_viewset)
router.register(r'equipos',equipo_viewset)
router.register(r'jugadores',jugador_viewset)
router.register(r'categorias',categoria_viewset)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls',namespace='rest_framework'))
]
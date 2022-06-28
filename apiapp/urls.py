from xml.etree.ElementInclude import include
from django.urls import path, include
from rest_framework import routers
from .views import *


router = routers.DefaultRouter()
router.register('producto', ProductoViewSet )
router.register('tipoproducto', TipoProductoViewSet )
router.register('cliente', ClienteViewSet )
router.register('tipocliente', TipoClienteViewSet )

urlpatterns = [
    path('api/', include(router.urls)),
]
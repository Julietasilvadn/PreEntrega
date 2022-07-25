from django.contrib import admin
from django.urls import path, include
from pantallas.views import *
from django.conf import settings
from pantallas.urls import pantallas_patterns
from app_entrega.views import mostrar_index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('pantallas/', include(pantallas_patterns)),    
    path('', mostrar_index, name='index'),
]

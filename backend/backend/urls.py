"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from rest_framework import routers
from apps.plano import views

router_v1 = routers.DefaultRouter()
router_v1.register(r'plano', views.PlanoViewSet)
router_v1.register(r'planoUsuario', views.PlanoUsuarioViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router_v1.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

from .models import Plano, PlanoUsuario
from rest_framework import viewsets
from .serializers import PlanoSerializer, PlanoUsuarioSerializer

class PlanoViewSet(viewsets.ModelViewSet):
    queryset = Plano.objects.all()
    serializer_class = PlanoSerializer

class PlanoUsuarioViewSet(viewsets.ModelViewSet):
    queryset = PlanoUsuario.objects.all()
    serializer_class = PlanoUsuarioSerializer
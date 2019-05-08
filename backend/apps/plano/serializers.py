from django.contrib.auth.models import User, Group
from .models import Plano, PlanoUsuario
from rest_framework import serializers

class PlanoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plano
        fields = ('__all__')

class PlanoUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanoUsuario
        fields = ('__all__')

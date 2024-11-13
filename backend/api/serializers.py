from django.contrib.auth.models import User
from rest_framework import serializers 
from .models import Note
# Clase que se encarga de serializar los atributos de los usuarios que se creen,
# para convertirlos en JSON
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}} #Esto hace que en la respuesta del backend no se mande la contraseña

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data);
        return user

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id","title","content","created_at", "author"]
        extra_kwargs = {"author": {"read_only": True}}
    
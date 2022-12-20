from rest_framework import serializers
from apps.users.models import User, Location, UserDate

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


    def to_representation(self, instance):
        return {
            'id' : instance.id,
            'nombres' : instance.nombres,
            'apellidos' : instance.apellidos,
        }


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class UserDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDate
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id' : instance.id,
            'telf' : instance.telf,
            'user' : instance.user.email,
        }
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.users.models import User, Location, UserDate
from apps.apis.serializers.users import UserSerializer, LocationSerializer, UserDateSerializer

class userListAPIView(APIView):
    def get(self, request):
        users = User.objects.all()
        users_serializer = UserSerializer(users, many = True)
        return Response(users_serializer.data, status = status.HTTP_200_OK)


class userCreateAPIView(APIView):
    def post(self, request):
        user_serializer = UserSerializer(data = request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(user_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class userDetailAPIView(APIView):
    def get(self, request, pk):
        user = User.objects.filter(id = pk).first()
        users_serializer = UserSerializer(user)
        return Response(users_serializer.data, status = status.HTTP_200_OK)

    def put(self, request, pk):
        user = User.objects.filter(id = pk).first()
        user_serializer = UserSerializer(user, data = request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status = status.HTTP_202_ACCEPTED)
        else:
            return Response(user_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    #por seguridad quedara desabilitado
    #def delete(self, request, pk):
    #    user = User.objects.filter(id = pk).first()
    #    user.delete()
    #    return Response('eliminado')

class userLocationAPIView(APIView):
    def get(self, request):
        locations = Location.objects.all()
        l_serializer = LocationSerializer(locations, many = True)
        return Response(l_serializer.data, status = status.HTTP_200_OK)

    def post(self, request):
        l_serializer = LocationSerializer(data = request.data)
        if l_serializer.is_valid():
            l_serializer.save()
            return Response(l_serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(l_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class userLocationDetailAPIView(APIView):
    def get(self, request, pk):
        location = Location.objects.get(id = pk)
        l_serializer = LocationSerializer(location)
        return Response(l_serializer.data, status = status.HTTP_200_OK)

    def put(self, request, pk):
        location = Location.objects.get(id = pk)
        l_serializer = LocationSerializer(location, data = request.data)
        if l_serializer.is_valid():
            l_serializer.save()
            return Response(l_serializer.data, status = status.HTTP_202_ACCEPTED)
        else:
            return Response(l_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        location = Location.objects.get(id = pk)
        location.delete()
        return Response("Eliminado", status = status.HTTP_202_ACCEPTED)

class userDateListAPIView(APIView):
    def get(self, request):
        date = UserDate.objects.all()
        date_serializer = UserDateSerializer(date, many = True)
        return Response(date_serializer.data, status = status.HTTP_200_OK)

    def post(self, request):
        date_serializer = UserDateSerializer(data = request.data)
        if date_serializer.is_valid():
            date_serializer.save()
            return Response(date_serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(date_serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class userDateDetailAPIView(APIView):
    def get(self, request, pk):
        date = UserDate.objects.get(id = pk)
        date_serializer = UserDateSerializer(date)
        return Response(date_serializer.data, status = status.HTTP_200_OK)

    def put(self, request, pk):
        date = UserDate.objects.get(id = pk)
        date_serializer = UserDateSerializer(date, data = request.data)
        if date_serializer.is_valid():
            date_serializer.save()
            return Response(date_serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(date_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        date = UserDate.objects.get(id = pk)
        date.delete()
        return Response("Eliminado", status = status.HTTP_202_ACCEPTED)

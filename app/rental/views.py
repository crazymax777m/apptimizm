from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from user.models import User
from user.serializers import UserDetailSerializer, UserListSerializer
from .models import Car
from .serializers import CarSerializer


class CarView(ModelViewSet):
    """Default CRUD of a Car"""

    queryset = Car.objects.all()
    serializer_class = CarSerializer


class UserView(ModelViewSet):
    """User or Users display"""

    queryset = User.objects.all()

    def get_serializer_class(self):
        return UserListSerializer if self.action == 'list' else UserDetailSerializer


class AddCarView(APIView):
    """Add a Car to User"""

    def get(self, request, pk=None, car_pk=None):
        user = User.objects.get(pk=pk)
        car = Car.objects.get(pk=car_pk)
        user.cars.add(car)
        serializer = UserDetailSerializer(user)
        return Response(serializer.data)


class DeleteCarView(APIView):
    """Delete a Car from User"""

    def get(self, request, pk=None, car_pk=None):
        user = User.objects.get(pk=pk)
        car = Car.objects.get(pk=car_pk)
        user.cars.remove(car)
        serializer = UserDetailSerializer(user)
        return Response(serializer.data)


class UserCarsListView(APIView):
    """All User Cars"""

    def get(self, request, pk=None):
        cars = Car.objects.filter(user__pk=pk)
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)

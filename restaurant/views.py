from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, MenuSerializer, BookingSerializer
from django.contrib.auth.models import User
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from .models import Menu, Booking
# Create your views here.

def index(request):
    return render(request, 'index.html', {})


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    

class MenuItemView(ListCreateAPIView):
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()

class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()

class BookingViewSet(ModelViewSet):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
    permission_classes = [IsAuthenticated]




from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Menu, Booking, MenuItem
from .serializers import MenuSerializer, UserSerializer, BookingSerializer, MenuItemSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import generics


# Create your views here.
def index(request):
    return render(request, 'index.html', {})


class MenuItemViewSet (viewsets.ViewSet):
    def list(self, request):
        query_set = Menu.objects.all()
        for x in query_set:
            print(x)
        menuSerializer =  MenuSerializer(query_set, many=True)
        print(menuSerializer.data)
        return Response(menuSerializer.data)
    
class UserViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)


class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        query_set = Booking.objects.all()
        serializer_class = BookingSerializer(query_set)
        return Response(serializer_class.data)
    
    
class BookingSet(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = Booking.objects.all()
        # import pdb;pdb.set_trace()
        serializer_class = BookingSerializer(queryset)
        permission_classes = [IsAuthenticated]
        print(serializer_class.data)
        return Response(serializer_class.data)
    

class MenuItemViews(generics.ListCreateAPIView):
    queryset=MenuItem.objects.all()
    serializer_class = MenuItemSerializer
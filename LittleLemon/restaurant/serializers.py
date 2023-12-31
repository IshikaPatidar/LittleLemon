from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Menu, Booking, MenuItem


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']
        
        
class MenuSerializer(serializers.Serializer):
    class Meta:
        model = Menu
        fields = ['id', 'MenuId', 'Title', 'Price', 'Inventory']
        
        
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
        

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'inventory']
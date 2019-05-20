from rest_framework import serializers
from .models import *


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = "__all__"


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = "__all__"


class MenuCategorySerializer(serializers.ModelSerializer):
    menu_items = MenuItemSerializer(many=True, read_only=True)

    class Meta:
        model = MenuCategory
        fields = ("name", "menu_items")

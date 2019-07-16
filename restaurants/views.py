from django.shortcuts import render
from rest_framework import viewsets
from .models import Restaurant
from .serializers import *
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.


class RestaurantViewSet(viewsets.ModelViewSet):
    """
    Provides a get method handler.
    """
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    @action(detail=True)
    def menu_items(self, request, pk=None):
        restaurant = self.get_object()
        category_items = restaurant.list_items_by_category()
        serializer = MenuCategorySerializer(category_items, many=True)
        return Response(serializer.data)


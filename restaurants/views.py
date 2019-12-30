from django.shortcuts import render
from rest_framework import viewsets
from .models import Restaurant
from .serializers import *
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, CustomObjectPermissions
from rest_framework_guardian import filters


class RestaurantViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,
                          CustomObjectPermissions,
                          )
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    # Not needed for now... pairs with django guardian to allow filtering of specific model instances
    # filter_backends = [filters.ObjectPermissionsFilter]

    @action(detail=True)
    def menu_items(self, request, pk=None):
        restaurant = self.get_object()
        category_items = restaurant.list_items_by_category()
        serializer = MenuCategorySerializer(category_items, many=True)
        return Response(serializer.data)


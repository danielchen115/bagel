from django.urls import path
from rest_framework_nested import routers
from .views import RestaurantViewSet


router = routers.SimpleRouter()
router.register(r'restaurants', RestaurantViewSet)

urlpatterns = router.urls
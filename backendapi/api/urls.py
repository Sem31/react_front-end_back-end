from .views import UserViewSet
from django.urls import path,include
from rest_framework import routers

router = routers.DefaultRouter()
router.register('users',UserViewSet)


urlpatterns =router.urls
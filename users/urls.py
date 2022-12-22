from django.urls import re_path,include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

router = DefaultRouter()
router.register(r'users',UserViewSet)

urlpatterns = [
    re_path(r"", include (router.urls)),
]
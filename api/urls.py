from django.urls import path, include
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register(r'signin', SignInViewSet)
router.register(r'signup', SignUpViewSet)


urlpatterns = [
    path('', include(router.urls)),
]

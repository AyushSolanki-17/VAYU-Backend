from django.urls import path, include
from rest_framework import routers

from copd.views import AbgTestViewSet, XrayTestViewSet, AbgAutoTestViewSet
from .views import *

router = routers.DefaultRouter()
router.register(r'signin', SignInViewSet)
router.register(r'signup', SignUpViewSet)
router.register(r'abgtest', AbgTestViewSet)
router.register(r'xraytest', XrayTestViewSet)
router.register(r'abgautotest', AbgAutoTestViewSet)


urlpatterns = [
    path('', include(router.urls)),
]

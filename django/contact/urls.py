from django.urls import path, include
from django.views.generic import TemplateView
from . import views
from rest_framework import routers 

router = routers.DefaultRouter()
router.register('', views.ContactViewSet)

urlpatterns = [
    path('', include(router.urls))
]



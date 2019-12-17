from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('teams', views.TeamViewSet)

urlpatterns = [
    path('api/2020/', include(router.urls)),
]

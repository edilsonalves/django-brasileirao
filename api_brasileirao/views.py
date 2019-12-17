from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from . import models, serializers


class TeamViewSet(viewsets.ModelViewSet):
    queryset = models.Team.objects.all().order_by('-points')
    serializer_class = serializers.TeamSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

from rest_framework import viewsets
from . import models, serializers


class TeamViewSet(viewsets.ModelViewSet):
    queryset = models.Team.objects.all().order_by('-points')
    serializer_class = serializers.TeamSerializer

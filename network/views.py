from rest_framework import viewsets
from .models import NetworkNode
from .serializers import NetworkNodeSerializer
from django_filters.rest_framework import DjangoFilterBackend


class NetworkNodeViewSet(viewsets.ModelViewSet):
    queryset = NetworkNode.objects.all()
    serializer_class = NetworkNodeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['country', 'city', 'type', 'supplier']
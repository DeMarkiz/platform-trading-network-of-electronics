from rest_framework import viewsets
from .models import NetworkNode
from .serializers import NetworkNodeSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .permissions import IsActiveStaff


class NetworkNodeViewSet(viewsets.ModelViewSet):
    queryset = NetworkNode.objects.all()
    serializer_class = NetworkNodeSerializer
    permission_classes = [IsActiveStaff]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['country', 'city', 'type', 'supplier']
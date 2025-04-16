from django.urls import path, include
from rest_framework.routers import DefaultRouter
from network.views import NetworkNodeViewSet
from django.contrib import admin


router = DefaultRouter()
router.register(r'network', NetworkNodeViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
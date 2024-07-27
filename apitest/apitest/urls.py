from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import AdvertisementViewSet

router_v1 = DefaultRouter()
router_v1.register(r'advertisements',
                   AdvertisementViewSet,
                   basename='advertisements')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router_v1.urls),),
    path('api/', include('djoser.urls')),
    path('api/', include('djoser.urls.jwt')),
]

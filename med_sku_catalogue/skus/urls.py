from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MedicationSKUViewSet

router = DefaultRouter()
router.register(r'skus', MedicationSKUViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

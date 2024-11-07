from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

# Import the necessary model and serializer
from .models import MedicationSKU
from .serializers import MedicationSKUSerializer

class MedicationSKUViewSet(viewsets.ModelViewSet):
    queryset = MedicationSKU.objects.all() 
    serializer_class = MedicationSKUSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filterset_fields = ['name', 'presentation', 'dose', 'unit']
    search_fields = ['name', 'presentation', 'dose', 'unit']
    ordering_fields = ['name', 'dose', 'presentation', 'unit']
    ordering = ['name'] 

    @action(detail=False, methods=['post'])
    def bulk_create(self, request):

        serializer = MedicationSKUSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()  # Save the bulk data
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

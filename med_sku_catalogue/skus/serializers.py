from rest_framework import serializers
from .models import MedicationSKU

class MedicationSKUSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicationSKU
        fields = '__all__'

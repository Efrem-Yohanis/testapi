# dealers/serializers.py
from rest_framework import serializers
from .models import Dealer1

class DealerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dealer1
        fields = '__all__'
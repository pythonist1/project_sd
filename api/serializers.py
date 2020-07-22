from rest_framework import serializers

from main.models import Deal, AdvUser

class DealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deal
        fields = ('__all__')
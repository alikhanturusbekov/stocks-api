from rest_framework import serializers

from .constants import SUPPORTED_STOCKS, ErrorMessage
from .models import CompanyNews


class CompanyNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyNews
        fields = '__all__'

    def validate(self, data):
        if data['stock'] not in SUPPORTED_STOCKS:
            raise serializers.ValidationError(ErrorMessage.INVALID_STOCK)

        return data

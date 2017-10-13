from rest_framework import serializers
from .models import Stocklist, Stock

class StocklistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stocklist
        fields = '__all__'
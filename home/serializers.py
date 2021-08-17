from rest_framework import serializers
from main.models import Main


class HomeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Main
        fields = '__all__'

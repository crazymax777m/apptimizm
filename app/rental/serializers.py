from rest_framework import serializers

from rental.models import Car


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['name', 'create_year', 'add_date']

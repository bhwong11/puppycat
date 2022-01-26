from rest_framework import serializers

from .models import Vacation


class VacationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vacation
        fields = ('place', 'days_off', 'cool')

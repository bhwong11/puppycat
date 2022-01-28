from rest_framework import serializers

from .models import Vacation, Activities


class ActivitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activities
        fields = '__all__'
        depth = 1


class VacationSerializer(serializers.Serializer):
    place = serializers.CharField(max_length=200)
    days_off = serializers.IntegerField()
    cool = serializers.BooleanField()

    def create(self, validated_data):
        return Vacation.objects.create(**validated_data)

    def update(self, instance, validated_data):
        print('VALIDATED DATA', validated_data)
        instance.place = validated_data.get('place', instance.place)
        instance.days_off = validated_data.get('days_off', instance.days_off)
        instance.cool = validated_data.get('cool', instance.cool)
        instance.save()
        return instance

    # class Meta:
    #    model = Vacation
    #    fields = ('vacation_id', 'place', 'days_off', 'cool')

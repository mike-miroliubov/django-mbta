from rest_framework.serializers import ModelSerializer

from django_intro_app.models import Station


class StationSerializer(ModelSerializer):
    class Meta:
        model = Station
        fields = ['id', 'name']
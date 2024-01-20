from rest_framework.response import Response
from rest_framework.views import APIView

from django_intro_app.exception.invalid_input_exception import InvalidInputException
from django_intro_app.models import Station
from django_intro_app.services import station_service
from django_intro_app.view.serializers.station_serializer import StationSerializer
from django_intro_app.view.views import handle_exceptions


class BranchStationAPI(APIView):
    @handle_exceptions
    def get(self, request, branch_id) -> Response:
        return Response({
            'stations': StationSerializer(station_service.get_stations_by_branch_id(branch_id), many=True).data
        })


class StationAPI(APIView):
    @handle_exceptions
    def get(self, request, id) -> Response:
        try:
            return Response(StationSerializer(Station.objects.get(id=id)).data)
        except Station.DoesNotExist:
            raise InvalidInputException('Station with id %s does not exist' % id)
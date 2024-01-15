from rest_framework.response import Response
from rest_framework.views import APIView

from django_intro_app.exception.invalid_input_exception import InvalidInputException
from django_intro_app.models import Station, Branch
from django_intro_app.view.serializers.station_serializer import StationSerializer
from django_intro_app.view.views import handle_exceptions


class BranchStationAPI(APIView):
    @handle_exceptions
    def get(self, request, branch_id) -> Response:
        try:
            branch = Branch.objects.get(id=branch_id)
        except Branch.DoesNotExist:
            raise InvalidInputException('Branch with id %s does not exist' % branch_id)

        return Response({
            'stations': StationSerializer(branch.stations, many=True).data
        })


class StationAPI(APIView):
    @handle_exceptions
    def get(self, request, id) -> Response:
        try:
            return Response(StationSerializer(Station.objects.get(id=id)).data)
        except Station.DoesNotExist:
            raise InvalidInputException('Station with id %s does not exist' % id)
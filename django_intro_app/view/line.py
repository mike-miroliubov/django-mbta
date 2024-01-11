from django.http import HttpRequest, JsonResponse
from rest_framework.decorators import api_view

from .serializers.LineSerializer import LineSerializer
from .views import handle_exceptions
from ..models import Line
from ..service.line_service import LineService

line_service = LineService()


@api_view(['GET'])
@handle_exceptions
def get_line(request: HttpRequest, id: str):
    return JsonResponse(LineSerializer(line_service.get_line(id)).data)


@api_view(['GET'])
@handle_exceptions
def list_lines(request: HttpRequest):
    return JsonResponse({
        'lines': LineSerializer(Line.objects.all(), many=True).data
    })
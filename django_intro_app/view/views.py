import functools
import uuid
from typing import List

from django.http import JsonResponse, HttpRequest, HttpResponseBadRequest, HttpResponseServerError, HttpResponse
from django.shortcuts import render
from django.template import loader

from django_intro_app.exception.invalid_input_exception import InvalidInputException
from django_intro_app.models import Line
from django_intro_app.service.line_service import LineService
from django_intro_app.view.serializers.LineSerializer import LineSerializer


# Create your views here.
line_service = LineService()


def list_stations(request: HttpRequest):
    return JsonResponse({
        'stations': [{
            'id': uuid.uuid1(),
            'name': '1 OK Rock'
        }]
    })


def handle_exceptions(func):
    @functools.wraps(func)
    def handler(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except InvalidInputException as e:
            return HttpResponseBadRequest(JsonResponse({'error': str(e)}))
        except Exception as e:
            return HttpResponseServerError(JsonResponse({'error': str(e)}))

    return handler


@handle_exceptions
def get_line(request: HttpRequest, id: str):
    return JsonResponse(LineSerializer(line_service.get_line(id)).data)


@handle_exceptions
def list_lines(request: HttpRequest):
    return JsonResponse({
        'lines': LineSerializer(Line.objects.all(), many=True).data
    })


def lines_view(request: HttpRequest):
    lines: List[Line] = Line.objects.all()
    branches_by_line = {l: l.branch_set.all() for l in lines}
    context = {
        'lines': [(l, branches_by_line[l]) for l in lines]
    }

    return render(request, 'lines/index.html', context)
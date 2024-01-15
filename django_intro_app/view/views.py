import functools
import logging
import uuid
from typing import List

from django.core.exceptions import ValidationError
from django.http import JsonResponse, HttpRequest, HttpResponseBadRequest, HttpResponseServerError
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from rest_framework.decorators import api_view

from django_intro_app.exception.invalid_input_exception import InvalidInputException
from django_intro_app.models import Line

# Create your views here.


@api_view(['GET'])
def list_stations(request: HttpRequest):
    return JsonResponse({
        'stations': [{
            'id': uuid.uuid1(),
            'name': '1 OK Rock'
        }]
    })

logger = logging.getLogger('main')


def handle_exceptions(func):
    # to correctly preserve original function name and parameters use @functools.wraps(func)
    @functools.wraps(func)
    def handler(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (InvalidInputException, ValidationError) as e:
            logger.exception('exception')
            return HttpResponseBadRequest(JsonResponse({'error': str(e)}))
        except Exception as e:
            logger.exception('exception')
            return HttpResponseServerError(JsonResponse({'error': str(e)}))

    return handler


@require_http_methods(['GET'])
def lines_view(request: HttpRequest):
    lines: List[Line] = Line.objects.all()
    branches_by_line = {l: l.branch_set.all() for l in lines}
    context = {
        'lines': [(l, branches_by_line[l]) for l in lines]
    }

    return render(request, 'lines/index.html', context)
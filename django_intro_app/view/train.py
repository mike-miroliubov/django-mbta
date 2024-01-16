import logging
import uuid

from django.db import IntegrityError
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from django_intro_app.exception.invalid_input_exception import InvalidInputException
from django_intro_app.models import Train, TrainRegistration
from django_intro_app.utils.authentication import TrackingDeviceAuthentication
from django_intro_app.view.views import handle_exceptions


class TrainRegistrationAPI(APIView):
    authentication_classes = [TrackingDeviceAuthentication]
    permission_classes = [IsAuthenticated]
    log = logging.getLogger('main')

    @handle_exceptions
    def post(self, request, id: str) -> Response:
        try:
            train: Train = Train.objects.get(id=id)
        except Train.DoesNotExist:
            raise InvalidInputException('Train with id %s does not exist' % id)

        registration = TrainRegistration.objects.filter(train=train)
        if registration:
            if registration[0].tracking_device == request.user:
                # This is a duplicate request, do nothing
                return Response(status=status.HTTP_202_ACCEPTED)

            raise InvalidInputException('Train %s:%s is already in operation' % (id, train.name))

        try:
            TrainRegistration.objects.create(id=uuid.uuid4(), train=train, tracking_device=request.user)
        except IntegrityError:
            raise InvalidInputException('Tracking device is already registered for a train')

        return Response(status=status.HTTP_202_ACCEPTED)
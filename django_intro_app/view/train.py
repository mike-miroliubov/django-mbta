import logging

from injector import inject
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from django_intro_app.services import TrainService
from django_intro_app.utils.authentication import TrackingDeviceAuthentication
from django_intro_app.view.views import handle_exceptions


class TrainRegistrationAPI(APIView):
    authentication_classes = [TrackingDeviceAuthentication]
    permission_classes = [IsAuthenticated]
    log = logging.getLogger('main')

    @inject
    def __init__(self, train_service: TrainService):
        self.train_service = train_service
        super().__init__()

    @handle_exceptions
    def post(self, request, id: str) -> Response:
        self.train_service.register_tracking_device(request.user, id)
        return Response(status=status.HTTP_202_ACCEPTED)

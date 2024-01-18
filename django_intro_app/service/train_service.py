import logging
import uuid

from django.db import IntegrityError

from django_intro_app.exception.invalid_input_exception import InvalidInputException
from django_intro_app.models import Train, TrainRegistration, TrackingDevice


class TrainService:
    log = logging.getLogger('main')

    def register_tracking_device(self, tracking_device: TrackingDevice, train_id: str):
        self.log.info('register_tracking_device(%s)', locals())

        try:
            train: Train = Train.objects.get(id=train_id)
        except Train.DoesNotExist:
            raise InvalidInputException('Train with id %s does not exist' % train_id)

        registration = TrainRegistration.objects \
            .select_related('tracking_device') \
            .filter(train=train)
        if registration:
            if registration[0].tracking_device == tracking_device:
                # This is a duplicate request, do nothing
                return

            raise InvalidInputException('Train %s:%s is already in operation' % (train_id, train.name))

        try:
            TrainRegistration.objects.create(id=uuid.uuid4(), train=train, tracking_device=tracking_device)
        except IntegrityError:
            raise InvalidInputException('Tracking device is already registered for a train')
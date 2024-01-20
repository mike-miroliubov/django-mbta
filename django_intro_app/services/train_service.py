import logging
import uuid

from django.db import IntegrityError
from injector import inject

from django_intro_app.exception.invalid_input_exception import InvalidInputException
from django_intro_app.models import Train, TrainRegistration, TrackingDevice
from django_intro_app.repository import TrainRepository


class TrainService:
    log = logging.getLogger('main')

    @inject
    def __init__(self, train_repository: TrainRepository):
        self.train_repository = train_repository

    def register_tracking_device(self, tracking_device: TrackingDevice, train_id: str):
        self.log.info('register_tracking_device(%s)', locals())

        try:
            train: Train = self.train_repository.get_by_id(train_id)
        except Train.DoesNotExist:
            raise InvalidInputException('Train with id %s does not exist' % train_id)

        registration = self.train_repository.find_registration_by_train(train)
        if registration:
            if registration[0].tracking_device == tracking_device:
                # This is a duplicate request, do nothing
                return

            raise InvalidInputException('Train %s:%s is already in operation' % (train_id, train.name))

        try:
            self.train_repository.create_registration(
                TrainRegistration(id=uuid.uuid4(), train=train, tracking_device=tracking_device))
        except IntegrityError:
            raise InvalidInputException('Tracking device is already registered for a train')
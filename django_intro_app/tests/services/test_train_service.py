import uuid
from unittest import TestCase

from django_intro_app.models import TrackingDevice, Train, Branch, Line, TrainRegistration
from django_intro_app.services.train_service import TrainService


class TrainServiceTest(TestCase):
    service = TrainService()

    def test_register_tracking_device(self):
        # given
        device = TrackingDevice.objects.create(id=uuid.uuid4(), api_key='test_key')
        line = Line.objects.create(id=uuid.uuid4(), name='TestLine', color='transparent')
        branch = Branch.objects.create(id=uuid.uuid4(), name='TestBranch', line=line)
        train = Train.objects.create(id=uuid.uuid4(), name='TstTrain', branch=branch)

        # when
        self.service.register_tracking_device(device, train.id)

        # then
        registration: TrainRegistration = TrainRegistration.objects.select_related('tracking_device').get(train=train)
        self.assertEqual(registration.tracking_device, device)
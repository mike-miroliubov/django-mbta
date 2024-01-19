import uuid
from unittest.mock import Mock

from django.test import SimpleTestCase

from django_intro_app.models import TrackingDevice, Train
from django_intro_app.services.train_service import TrainService


class TrainServiceTest(SimpleTestCase):

    def test_register_tracking_device(self):
        # given
        TrainRepositoryMock = Mock()
        service = TrainService(TrainRepositoryMock)

        device = TrackingDevice(id=uuid.uuid4(), api_key='test_key')
        train_id = str(uuid.uuid4())

        train = Train(id=uuid.uuid4(), name='TstTrain')
        TrainRepositoryMock.get_by_id.return_value = train
        TrainRepositoryMock.find_registration_by_train.return_value = None

        # when
        service.register_tracking_device(device, train_id)

        # then
        registration = TrainRepositoryMock.create_registration.call_args[0][0]
        self.assertEqual(registration.train, train)
        self.assertEqual(registration.tracking_device, device)
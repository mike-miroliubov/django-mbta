import uuid
from unittest.mock import patch

from django.test import SimpleTestCase

from django_intro_app.models import Station
from django_intro_app.services import station_service


class StationServiceTest(SimpleTestCase):
    @patch('django_intro_app.models.Branch.objects.get')
    def test_get_stations_by_branch_id(self, BranchMock):
        # given
        stations = [Station(id=uuid.uuid4(), name='test1'), Station(id=uuid.uuid4(), name='test1')]
        BranchMock.return_value.stations = stations
        branch_id = uuid.uuid4()

        # when
        actual_stations = station_service.get_stations_by_branch_id(branch_id)

        # then
        self.assertIs(actual_stations, stations)



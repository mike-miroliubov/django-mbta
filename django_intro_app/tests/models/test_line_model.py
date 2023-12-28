import uuid

from django.test import TestCase

from django_intro_app.models import Line


class LineModelTests(TestCase):
    def test_should_find_all_lines(self):
        # given
        white = Line.objects.create(id=uuid.uuid4(), name='Test Line', color='white')
        black = Line.objects.create(id=uuid.uuid4(), name='Test Line', color='black')

        # when
        lines = Line.objects.all()

        # then
        print(lines)
        # logging.info(lines)
        self.assertQuerySetEqual(set(lines), {black, white}, ordered=False)

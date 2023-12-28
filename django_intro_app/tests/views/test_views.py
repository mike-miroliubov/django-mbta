import uuid

from django.http import JsonResponse
from django.test import TestCase

from django_intro_app.models import Line


class LineViewTest(TestCase):
    def test_list_lines(self):
        # given
        Line.objects.create(id=uuid.UUID('f413cbf3-adf7-4c89-bc97-ef4237698d61'),
                            name='Test Line', color='white')
        Line.objects.create(id=uuid.UUID('fafc00ca-188f-46ca-9a3f-ce53982d0c35'),
                            name='Test Line2', color='black')

        # when
        response: JsonResponse = self.client.get("/api/v1/lines/")

        # then
        self.assertJSONEqual(str(response.content, encoding='utf-8'), '''
            {
                "lines": [
                    {
                        "id": "f413cbf3-adf7-4c89-bc97-ef4237698d61",
                        "name": "Test Line",
                        "color": "white" 
                    },
                    {
                        "id": "fafc00ca-188f-46ca-9a3f-ce53982d0c35",
                        "name": "Test Line2",
                        "color": "black"
                    }
                ]
            }''')

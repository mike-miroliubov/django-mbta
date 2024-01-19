import uuid

from django.http import JsonResponse
from django.test import TestCase

from django_intro_app.models import Line


class LineViewTest(TestCase):
    def test_list_lines(self):
        # given

        # when
        response: JsonResponse = self.client.get("/api/v1/lines/")

        # then
        self.assertJSONEqual(str(response.content, encoding='utf-8'), '''
            {
                "lines": [
                    {
                        "id": "f88c33b8-02bf-4abb-8b35-f4d063d39a2d",
                        "name": "Green Line",
                        "color": "green"
                    },
                    {
                        "id": "3d33d693-59da-42e3-a010-8bc228239a10",
                        "name": "Red Line",
                        "color": "red"
                    },
                    {
                        "id": "cbf157c8-22b0-49cd-8f75-ce62935b7283",
                        "name": "Orange Line",
                        "color": "orange"
                    },
                    {
                        "id": "af55a708-cf8e-4a72-9d2c-af1f3a1aed32",
                        "name": "Blue Line",
                        "color": "blue"
                    },
                    {
                        "id": "58369f1a-6f68-4341-8a69-9de55ecfeb1e",
                        "name": "Silver Line",
                        "color": "silver"
                    }
                ]
            }''')

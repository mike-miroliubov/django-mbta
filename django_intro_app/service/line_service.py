import uuid

from django_intro_app.exception.invalid_input_exception import InvalidInputException
from django_intro_app.models import Line


class LineService:
    def get_line(self, id: str) -> Line:
        try:
            line_uuid = uuid.UUID(id)
        except ValueError:
            raise InvalidInputException('Invalid input id=%s' % id)

        try:
            return Line.objects.get(id=line_uuid)
        except Line.DoesNotExist:
            raise InvalidInputException('Line with id %s does not exist' % id)
from django_intro_app.exception.invalid_input_exception import InvalidInputException
from django_intro_app.models import Branch, Station


# Example of functional service without dependency injection
def get_stations_by_branch_id(branch_id: str) -> list[Station]:
    try:
        return Branch.objects.get(id=branch_id).stations
    except Branch.DoesNotExist:
        raise InvalidInputException('Branch with id %s does not exist' % branch_id)
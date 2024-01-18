import uuid

from django_intro_app.exception.invalid_input_exception import InvalidInputException
from django_intro_app.models import Line, Branch, Direction


class BranchService:
    def create_branch(self, line_id: str, name: str, direction: Direction) -> Branch:
        try:
            line = Line.objects.get(id=line_id)
        except Line.DoesNotExist:
            raise InvalidInputException('Line with id %s does not exist' % line_id)

        new_branch = Branch(id=uuid.uuid4(), name=name, line=line, direction=direction)
        new_branch.save()

        return new_branch

    def find_branches_by_line(self, line_id: str) -> list[Branch]:
        return Branch.objects.filter(line=line_id)

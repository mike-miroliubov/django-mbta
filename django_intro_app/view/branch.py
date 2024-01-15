from rest_framework.response import Response
from rest_framework.views import APIView

from django_intro_app.exception.invalid_input_exception import InvalidInputException
from django_intro_app.models import Branch, Line
from django_intro_app.view.serializers.branch_serializer import BranchSerializer
from django_intro_app.view.views import handle_exceptions


class BranchAPI(APIView):
    @handle_exceptions
    def get(self, request, id: str) -> Response:
        return Response(BranchSerializer(Branch.objects.get(id=id)).data)


class LineBranchAPI(APIView):
    @handle_exceptions
    def get(self, request, line_id):
        branches = Branch.objects.filter(line=line_id)
        return Response({
            'branches': BranchSerializer(branches, many=True).data
        })

    @handle_exceptions
    def post(self, request, line_id) -> Response:
        try:
            line = Line.objects.get(id=line_id)
        except Line.DoesNotExist:
            raise InvalidInputException('Line with id %s does not exist' % line_id)

        serialized = BranchSerializer(data=request.data)
        serialized.is_valid(raise_exception=True)
        new_branch = Branch(**serialized.validated_data)
        new_branch.line = line
        new_branch.save()

        return Response(BranchSerializer(new_branch).data)

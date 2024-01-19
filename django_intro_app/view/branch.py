from injector import inject
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from django_intro_app.models import Branch, Direction
from django_intro_app.services.branch_service import BranchService
from django_intro_app.view.views import handle_exceptions


class BranchAPI(APIView):
    class OutputSerializer(serializers.Serializer):
        id = serializers.UUIDField()
        name = serializers.CharField()
        direction = serializers.ChoiceField(choices=Direction)

    @handle_exceptions
    def get(self, request, id: str) -> Response:
        return Response(self.OutputSerializer(Branch.objects.get(id=id)).data)


class LineBranchAPI(APIView):
    class OutputSerializer(serializers.Serializer):
        id = serializers.UUIDField()
        name = serializers.CharField()
        direction = serializers.ChoiceField(choices=Direction)

    class InputSerializer(serializers.Serializer):
        name = serializers.CharField()
        direction = serializers.ChoiceField(choices=Direction)

    @inject
    def __init__(self, branch_service: BranchService):
        self.branch_service = branch_service
        super().__init__()

    @handle_exceptions
    def get(self, request, line_id):
        return Response({
            'branches': self.OutputSerializer(self.branch_service.find_branches_by_line(line_id), many=True).data
        })

    @handle_exceptions
    def post(self, request, line_id) -> Response:
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        branch = self.branch_service.create_branch(line_id, **serializer.validated_data)

        return Response(self.OutputSerializer(branch).data)

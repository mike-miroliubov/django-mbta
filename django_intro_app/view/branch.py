from rest_framework.response import Response
from rest_framework.views import APIView

from django_intro_app.models import Branch
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

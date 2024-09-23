from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated

from apps.users.models import User
from apps.users.permissions import IsAdmin
from apps.users.api_endpoints.Admin.serializers import UserStatisticsSerializer


class AdminAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated, IsAdmin)
    serializer_class = UserStatisticsSerializer
    queryset = User.objects.all()

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(instance=self.get_queryset(), many=True)
        return Response(serializer.data)



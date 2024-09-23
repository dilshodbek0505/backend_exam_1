from rest_framework.permissions import IsAuthenticated

from apps.course.models import UserCourse
from apps.course.api_endpoints.UserCourse.serializers import UserCourseSerializer
from apps.course.permissions import IsAdmin

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class UserCourseAPIView(ListCreateAPIView):
    queryset = UserCourse.objects.all()
    serializer_class = UserCourseSerializer
    permission_classes = (IsAuthenticated, IsAdmin)


class UserCourseRUDAPIView(RetrieveUpdateDestroyAPIView):
    queryset = UserCourse.objects.all()
    serializer_class = UserCourseSerializer
    permission_classes = (IsAuthenticated, IsAdmin)



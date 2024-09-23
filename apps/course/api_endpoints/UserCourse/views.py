from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from apps.course.permissions import IsAdmin
from apps.course.models import UserCourse
from apps.course.api_endpoints.UserCourse.serializers import UserCourseSerializer


class UserCourseListCreateAPIView(ListCreateAPIView):
    queryset = UserCourse.objects.all()
    serializer_class = UserCourseSerializer
    permission_classes = (IsAuthenticated, IsAdmin)


class UserCourseRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = UserCourse.objects.all()
    serializer_class = UserCourseSerializer
    permission_classes = (IsAuthenticated, IsAdmin)


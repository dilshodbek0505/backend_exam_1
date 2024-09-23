from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, RetrieveAPIView

from apps.course.models import Course
from apps.course.api_endpoints.Course.serializers import CourseSerializer
from apps.course.permissions import IsAdmin


class CourseCreateAPIView(CreateAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = (IsAuthenticated, IsAdmin)


class CourseRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = (IsAuthenticated, IsAdmin)


class CourseListAPIView(ListAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = (IsAuthenticated, )


class CourseRetrieveAPIView(RetrieveAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = (IsAuthenticated, )


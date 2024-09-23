from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from apps.course.api_endpoints.Video.serializers import VideoSerializer
from apps.course.models import Video
from apps.course.permissions import IsAdmin


class VideoCreateAPIView(CreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = (IsAuthenticated, IsAdmin)


class VideoRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = (IsAuthenticated, IsAdmin)


class VideoListAPIView(ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class VideoRetrieveAPIView(RetrieveAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer



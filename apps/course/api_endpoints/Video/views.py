from apps.course.models import Video
from apps.course.api_endpoints.Video.serializers import VideoSerializer
from apps.course.permissions import IsAdmin

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, ListAPIView,  RetrieveAPIView
from rest_framework.permissions import IsAuthenticated


class VideoAPIView(CreateAPIView):
    serializer_class = VideoSerializer
    queryset = Video.objects.all()
    permission_classes = (IsAuthenticated, IsAdmin)


class VideoRUDAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = VideoSerializer
    queryset = Video.objects.all()
    permission_classes = (IsAuthenticated, IsAdmin)


class VideoListAPIView(ListAPIView):
    serializer_class = VideoSerializer
    queryset = Video.objects.all()
    permission_classes = (IsAuthenticated,)


class VideoRetrieveAPIView(RetrieveAPIView):
    serializer_class = VideoSerializer
    queryset = Video.objects.all()
    permission_classes = (IsAuthenticated, )



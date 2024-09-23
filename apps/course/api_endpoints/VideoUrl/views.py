import hashlib, os, hmac
from wsgiref.util import FileWrapper

from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated

from django.conf import settings
from django.http import StreamingHttpResponse

from apps.course.models import Video, UserCourse


class GenerateVideoUrl(GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = self.request.user
        video_id = self.kwargs['video_id']

        video = None

        try:
            video = Video.objects.get(pk=video_id)
        except Video.DoesNotExist:
            return Response({"data": "Video not found"}, status=404)

        try:
            UserCourse.objects.get(user=user, course=video.course)
        except UserCourse.DoesNotExist:
            return Response({"data": "User course not found"}, status=404)

        data = f"{user.id}:{video_id}"
        secret_key = settings.SECRET_KEY

        url = hmac.new(secret_key.encode(), data.encode(), hashlib.sha256).hexdigest()

        return Response({"video_url": url}, status=200)


class VideoStream(GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = self.request.user
        video_id = self.kwargs['video_id']
        video_url = self.kwargs['video_url']

        data = f"{user.id}:{video_id}"
        secret_key = settings.SECRET_KEY

        url = hmac.new(secret_key.encode(), data.encode(), hashlib.sha256).hexdigest()

        if url != video_url:
            return Response({"data": "not found"}, status=404)

        try:
            video = Video.objects.get(pk=video_id)
        except Video.DoesNotExist:
            return Response({"data": "Video not found"}, status=404)

        try:
            UserCourse.objects.get(user=user, course=video.course)
        except UserCourse.DoesNotExist:
            return Response({"data": "User course not found"}, status=404)

        video_path = video.file.path

        if not os.path.exists(video_path):
            return Response({
                "data": "video url not found"
            }, status=404)

        content_type = 'video/mp4'
        response = StreamingHttpResponse(FileWrapper(open(video_path, 'rb')), content_type=content_type)
        return response





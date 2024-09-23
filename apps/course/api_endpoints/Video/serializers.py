from rest_framework import serializers

from apps.course.models import Video


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ("id", "name", "file", "course", "duration")
        read_only_fields = ("file", "duration")


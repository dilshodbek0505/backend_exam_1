from rest_framework import serializers

from apps.course.models import Video


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'
        write_only_fields = ("file",)

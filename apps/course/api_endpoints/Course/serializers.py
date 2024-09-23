from rest_framework import serializers

from apps.course.models import Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ("id", "title", "about", "duration", "author")
        read_only_fields = ("duration",)




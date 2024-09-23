from rest_framework import serializers

from apps.course.models import UserCourse


class UserCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCourse
        fields = ("id", "user", "course", "is_finished")
        read_only_fields = ("is_finished", )


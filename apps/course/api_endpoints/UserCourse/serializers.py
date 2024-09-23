from rest_framework import serializers

from apps.course.models import UserCourse


class UserCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCourse
        fields = '__all__'

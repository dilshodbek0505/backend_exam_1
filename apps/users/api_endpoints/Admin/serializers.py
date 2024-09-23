from django.db.models import Sum

from rest_framework import serializers

from apps.users.models import User
from apps.course.models import UserCourse, UserCourseVideo


class UserStatisticsSerializer(serializers.ModelSerializer):
    course_count = serializers.SerializerMethodField()
    progress = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "avatar", "role", "course_count", "progress")

    def get_course_count(self, obj):
        user_courses = UserCourse.objects.filter(user_id=obj.id).count()
        return user_courses

    def get_progress(self, obj):
        # Foydalanuvchi ishtirok etayotgan barcha kurslar
        user_courses = UserCourse.objects.filter(user_id=obj.id).values_list('course_id', flat=True)

        # Barcha kurslarning umumiy davomiyligi
        total_course_duration = \
        UserCourse.objects.filter(user_id=obj.id).aggregate(total_duration=Sum('course__duration'))['total_duration']

        if not total_course_duration:
            return 0  # Agar kurslar bo'lmasa, progress 0 bo'ladi

        # Foydalanuvchi tomonidan ko'rilgan videolarning umumiy davomiyligi
        total_watched_duration = \
        UserCourseVideo.objects.filter(user_id=obj.id, video__course_id__in=user_courses).aggregate(
            total_duration=Sum('duration'))['total_duration']

        if not total_watched_duration:
            return 0  # Agar hech qanday video tomosha qilinmagan bo'lsa, progress 0 bo'ladi

        # Foiz hisoblash
        progress_percentage = (total_watched_duration / total_course_duration) * 100

        return round(progress_percentage, 2)  # 2ta kasr joyini qoldiramiz





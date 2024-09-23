from django.contrib import admin
from .models import (
    Course,
    Video,
    UserCourse,
    UserCourseVideo
)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    ...


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    ...


@admin.register(UserCourse)
class UserCourseAdmin(admin.ModelAdmin):
    ...


@admin.register(UserCourseVideo)
class UserCourseVideoAdmin(admin.ModelAdmin):
    ...

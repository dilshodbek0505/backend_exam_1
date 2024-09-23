from datetime import timedelta

from django.db import models

from apps.common.models import BaseModel
from apps.users.models import User

from moviepy.editor import VideoFileClip


class Course(BaseModel):
    title = models.CharField(max_length=100)
    about = models.TextField(blank=True, null=True)
    duration = models.DurationField(default=0)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.title


class Video(BaseModel):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to="videos/")
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, blank=True, null=True)
    duration = models.DurationField(default=0)

    def save(
        self,
        *args,
        force_insert=False,
        force_update=False,
        using=None,
        update_fields=None,
    ):
        super().save(*args, force_insert, force_update, using, update_fields)

        if (self.file and not self.duration) or (self.file and self.duration and force_update):
            clip = VideoFileClip(self.file.path)
            self.duration = timedelta(clip.duration)
            self.save()
            self.course.duration += timedelta(clip.duration)
            self.course.save()

    def __str__(self):
        return self.name


class UserCourse(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True)
    is_finished = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.get_full_name()}-{self.course}'


class UserCourseVideo(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    video = models.ForeignKey(Video, on_delete=models.CASCADE, blank=True, null=True)
    duration = models.DurationField(default=0)

    def __str__(self):
        return f'{self.user.get_full_name()}-{self.video.name}'


from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from datetime import timedelta

from apps.course.models import UserCourse, Video, UserCourseVideo


@receiver(post_save, sender=UserCourse)
def create_user_course(sender, instance, created, **kwargs):
    if created:
        ids = Video.objects.filter(course=instance.course).values_list('id', flat=True)
        UserCourseVideo.objects.bulk_create(
            [UserCourseVideo(user=instance.user, video_id=video_id, duration=timedelta(seconds=0)) for video_id in ids])


@receiver(post_save, sender=Video)
def create_video(sender, instance, created, **kwargs):
    if created:
        user_ids = UserCourse.objects.filter(course=instance.course).values_list('user_id', flat=True)
        UserCourseVideo.objects.bulk_create([
            UserCourseVideo(user_id=user_id, video=instance, duration=timedelta(seconds=0)) for user_id in user_ids
        ])


@receiver(post_delete, sender=Video)
def delete_video(sender, instance, **kwargs):
    user_ids = UserCourse.objects.filter(course=instance.course).values_list('user_id', flat=True)
    UserCourseVideo.objects.filter(user_id__in=user_ids, video=instance).delete()
    instance.course.duration -= instance.duration
    instance.course.save()


@receiver(post_save, sender=UserCourseVideo)
def edit_user_course_video(sender, instance, created, **kwargs):
    if not created:
        total_duration = instance.video.course.duration.total_seconds()
        videos = Video.objects.filter(course=instance.video.course)
        user_course_videos = UserCourseVideo.objects.filter(user=instance.user, video__in=videos)
        total_user_duration = sum(
            user_course_video.duration.total_seconds() for user_course_video in user_course_videos)

        if total_user_duration > total_duration * 0.8:
            try:
                user_course = UserCourse.objects.get(user=instance.user, course=instance.video.course)
                user_course.is_finished = True
                user_course.save()
            except:
                ...

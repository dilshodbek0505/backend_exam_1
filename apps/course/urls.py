from django.urls import path
from apps.course.api_endpoints.VideoUrl.views import GenerateVideoUrl, VideoStream
from apps.course.api_endpoints.Course.views import (
    CourseCreateAPIView,
    CourseRetrieveUpdateDestroyAPIView,
    CourseListAPIView,
    CourseRetrieveAPIView
)
from apps.course.api_endpoints.Video.views import (
    VideoCreateAPIView,
    VideoRetrieveUpdateDestroyAPIView,
    VideoListAPIView,
    VideoRetrieveAPIView
)
from apps.course.api_endpoints.UserCourse.views import (
    UserCourseListCreateAPIView,
    UserCourseRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    # video
    path("generate-video-url/<uuid:video_id>/", GenerateVideoUrl.as_view()),
    path("video-url/<str:video_url>/<uuid:video_id>/", VideoStream.as_view()),

    # course
    path("courese-create/", CourseCreateAPIView.as_view()),
    path("course-list/", CourseListAPIView.as_view()),
    path("course-details/<uuid:pk>/", CourseRetrieveUpdateDestroyAPIView.as_view()),
    path("course-retrieve/<uuid:pk>/", CourseRetrieveAPIView.as_view()),

    # video
    path("video-create/", VideoCreateAPIView.as_view()),
    path("video-list/", VideoListAPIView.as_view()),
    path("video-details/<uuid:pk>/", VideoRetrieveUpdateDestroyAPIView.as_view()),
    path("video-retrieve/<uuid:pk>/", VideoRetrieveAPIView.as_view()),

    # user course
    path("user-course/", UserCourseListCreateAPIView.as_view()),
    path("user-course-details/<uuid:pk>/", UserCourseRetrieveUpdateDestroyAPIView.as_view())

]

from django.urls import path
from apps.users.api_endpoints.Auth.views import (
    OtpApi,
    RegisterApi,
    UserListApi,
    ConfirmOtpApi,
    UserDetailApi
)
from apps.users.api_endpoints.Admin.views import AdminAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



urlpatterns = [
    # user api
    path('register/', RegisterApi.as_view(), name='register'),
    path('otp/', OtpApi.as_view(), name='otp'),
    path('otp-confirm/', ConfirmOtpApi.as_view(), name='otp-confirm'),
    path('user-list/', UserListApi.as_view(), name='user-list'),
    path('user-detail/<int:pk>/', UserDetailApi.as_view(), name='user-detail'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin', AdminAPIView.as_view())

]

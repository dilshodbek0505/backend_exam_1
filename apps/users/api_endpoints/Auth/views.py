from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView
from rest_framework.permissions import IsAuthenticated

from apps.users.models import User
from apps.users.api_endpoints.Auth.serializers import UserSerializer, OtpSerializer, ConfirmOtpSerializer
from apps.users.api_endpoints.Auth.permissions import IsAdmin
from apps.users.api_endpoints.Auth.utile import generate_code

from django.utils.cache import caches


class RegisterApi(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserListApi(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAdmin]


class UserDetailApi(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


class OtpApi(GenericAPIView):
    serializer_class = OtpSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if caches.keys(f'otp_{serializer.validated_data["phone_number"]}'):
            return Response({"data": "sms_already_send"}, status=400)

        code = generate_code()

        caches.set(f'otp_{serializer.validated_data["phone_number"]}', code, 60 * 2)
        print(code)

        return Response({"data": "send_code"}, status=200)


class ConfirmOtpApi(GenericAPIView):
    serializer_class = ConfirmOtpSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        cache_code = caches.get(f'otp_{serializer.validated_data["phone_number"]}')

        if cache_code != serializer.validated_data["code"]:
            return Response({"data": "wrong_code"}, status=400)

        caches.delete(f'otp_{serializer.validated_data["phone_number"]}')

        return Response({"data": "ok"}, status=200)


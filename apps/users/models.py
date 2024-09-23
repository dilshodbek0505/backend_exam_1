from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel
from apps.users.enums import UserRoleEnum


class User(AbstractUser, BaseModel):
    phone_number = models.CharField(max_length=13, help_text=_("Phone number"), unique=True)
    bio = models.TextField(help_text=_("Bio"), blank=True, null=True)
    avatar = models.ImageField(upload_to="user_images/", default='default.jpg', help_text=_("Avatar"))
    role = models.CharField(max_length=50, choices=UserRoleEnum.get_role(), default='user', help_text=_("User role"))

    def __str__(self):
        return self.username

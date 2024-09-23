from enum import Enum


class UserRoleEnum(Enum):
    admin = 'admin'
    teacher = 'teacher'
    user = 'user'

    @classmethod
    def get_role(cls):
        return (
            (item.name, item.value) for item in cls
        )


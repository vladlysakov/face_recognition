from face.models import CustomUser


def save(user: CustomUser) -> None:
    user.save()

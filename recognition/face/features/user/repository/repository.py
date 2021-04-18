from face.features.user.repository.models import CustomUser


def save(user: CustomUser) -> None:
    user.save()


def get_user(pk: int) -> CustomUser:
    user = CustomUser.objects.get(pk=pk)

    return user

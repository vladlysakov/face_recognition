from face.models import FaceRecognition


def get_recognition_data(user_id: int):
    data = FaceRecognition.objects.filter(user=user_id)

    return data.first()

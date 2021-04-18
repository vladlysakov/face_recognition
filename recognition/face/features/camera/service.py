import cv2 as cv
import face_recognition

from face.common.exceptions import EncodingFaceException
from face.decorators import WithRetry


def get_image():
    cam = cv.VideoCapture(0)
    image = None

    cv.namedWindow("Press space to take a photo.", cv.WINDOW_NORMAL)
    cv.resizeWindow("Press space to take a photo.", 500, 400)

    while True:
        ret, frame = cam.read()

        if not ret:
            print("Failed to grab frame.")
            break

        cv.imshow("Press space to take a photo.", frame)
        k = cv.waitKey(1)

        if k % 256 == 27:
            print("Escape hit, closing...")
            break
        elif k % 256 == 32:
            image = frame
            break

    cam.release()
    cv.destroyAllWindows()

    return image


def encoding(image):
    rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)

    boxes = face_recognition.face_locations(rgb, model="hog")
    encodings = face_recognition.face_encodings(rgb, boxes)

    encodings_count = len(encodings)

    if encodings_count == 1:
        return encodings[0]
    elif encodings_count > 1:
        raise EncodingFaceException('Image should contain only 1 face.')
    else:
        raise EncodingFaceException('No face detected.')


@WithRetry(allowed_exceptions=(EncodingFaceException,))
def get_face_from_camera():
    image = get_image()
    image_encoding = encoding(image)

    return image_encoding

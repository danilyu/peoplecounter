import cv2
#import numpy as np

HAAR_CASCADE_XML_FILE_FACE = '/usr/share/opencv4/haarcascades/haarcascade_frontalface_default.xml'

def faceDetect():
    # Obtain face detection Haar cascade XML files from OpenCV
    face_cascade = cv2.CascadeClassifier(HAAR_CASCADE_XML_FILE_FACE)

    # Video Capturing class from OpenCV
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print(width, height)
    if cap.isOpened():
        cv2.namedWindow("Face Detection Window", cv2.WINDOW_AUTOSIZE)

        while True:
            return_key, image = cap.read()
            if not return_key:
                break

            grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            detected_faces = face_cascade.detectMultiScale(grayscale_image, 1.3, 5)

            # Create rectangle around the face in the image canvas
            for (x_pos, y_pos, width, height) in detected_faces:
                cv2.rectangle(image, (x_pos, y_pos), (x_pos + width, y_pos + height), (0, 0, 0), 2)

            cv2.imshow("Face Detection Window", image)

            key = cv2.waitKey(30) & 0xff
            # Stop the program on the ESC key
            if key == 27:
                break

        cap.release()
        cv2.destroyAllWindows()
    else:
        print("Cannot open Camera")

if __name__ == "__main__":
    faceDetect()
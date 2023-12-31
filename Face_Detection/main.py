import cv2
import os

__file__="PYTHON-PROJECT-1"
current_directory=os.path.dirname(os.path.abspath(__file__))

xml_folder=os.path.join(current_directory,"Face_Detection","data","xml_dosya")

face_cascade_path = os.path.join(xml_folder, 'haarcascade_frontalface_default.xml')
eye_cascade_path = os.path.join(xml_folder, 'haarcascade_eye.xml')


face_cascade = cv2.CascadeClassifier(face_cascade_path)
eye_cascade = cv2.CascadeClassifier(eye_cascade_path)
def detect(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 3)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
    return frame

video_capture = cv2.VideoCapture(0)

key=cv2.waitKey(0)
while True:
    _, frame = video_capture.read()
    canvas = detect(frame)
    cv2.imshow('Web Cam', canvas)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

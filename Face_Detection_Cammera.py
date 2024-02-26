import cv2

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

video_capture = cv2.VideoCapture(0)

while True:
    #  Capture frame par frame
    ret, frame = video_capture.read()

    image_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    detections = face_detector.detectMultiScale(image_gray, maxSize=(123, 123), minSize=(70, 70))

    #  Draw a rectangle around the faces
    for (x, y, w, h) in detections:
        print(w, h)
        cv2.rectangle(frame,(x, y), (x+w, y+h), (255, 255, 0), 3)

    #  Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.waitKey()
cv2.destroyAllWindows()

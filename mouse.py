import cv2
import numpy as np
import pyautogui
from scipy.spatial import distance as dist

# Load the cascades
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Function to detect eyes and calculate their center
def detect_eyes_and_center(frame, gray):
    eyes = eye_cascade.detectMultiScale(gray, 1.1, 3)
    eye_centers = []
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(frame, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
        eye_center = (int(ex + ew / 2), int(ey + eh / 2))
        eye_centers.append(eye_center)
    return eye_centers

# Function to calculate the eye aspect ratio (EAR)
def eye_aspect_ratio(eye):
    A = dist.euclidean(eye[1], eye[5])
    B = dist.euclidean(eye[2], eye[4])
    C = dist.euclidean(eye[0], eye[3])
    ear = (A + B) / (2.0 * C)
    return ear

cap = cv2.VideoCapture(0)
screen_width, screen_height = pyautogui.size()
border_margin = 50  # Set a margin to avoid the corners

# Variables for click detection
blink_threshold = 0.25
blink_frames = 2
consec_blinks = 0
blink_count = 0

# Variables for smooth mouse movement
num_avg_points = 5
avg_x = []
avg_y = []

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        eye_centers = detect_eyes_and_center(roi_color, roi_gray)
        if len(eye_centers) >= 2:
            left_eye, right_eye = eye_centers[:2]
            avg_eye_x = (left_eye[0] + right_eye[0]) / 2
            avg_eye_y = (left_eye[1] + right_eye[1]) / 2

            # Calculate the position to move the mouse cursor to
            move_x = int((avg_eye_x / w) * screen_width)
            move_y = int((avg_eye_y / h) * screen_height)

            # Ensure the mouse doesn't move to the corners
            move_x = max(border_margin, min(move_x, screen_width - border_margin))
            move_y = max(border_margin, min(move_y, screen_height - border_margin))

            # Smooth mouse movement
            avg_x.append(move_x)
            avg_y.append(move_y)
            if len(avg_x) > num_avg_points:
                avg_x.pop(0)
                avg_y.pop(0)
            smooth_x = int(sum(avg_x) / len(avg_x))
            smooth_y = int(sum(avg_y) / len(avg_y))
            pyautogui.moveTo(smooth_x, smooth_y)

    cv2.putText(frame, f"Blinks: {blink_count}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.imshow('Frame', frame)
    
    if cv2.waitKey(1) == 27:  # Esc key to exit
        break

cap.release()
cv2.destroyAllWindows()

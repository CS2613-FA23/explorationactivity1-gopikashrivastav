import cv2
import mediapipe as mp 
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.Hands() 
hands = mpHands.Hands


while True:
    success, img = cap.read()

    cv2.imshow("Image", img)
    cv2.waitKey(1)


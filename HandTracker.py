import cv2
import mediapipe as mp 
import time
import numpy as np 

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils


pTime = 0 #prev time is 0
cTime = 0 #curr time is 0


while True:
    success, img = cap.read()
    #converting to rgb 
    imgRGB= cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            #getting co-ordinates in each id
            #these are decimal values, not pixels
            #multiply by width and height to get pixel
            for id, lm in enumerate(handLms.landmark):
                print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                print(id, cx, cy)
                #In Hand Landmark Model, id=0 is wrist, id=4 is thumb_tip
                if id == 4:
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
            #mpHands.HANDCONNECTIONS draws connecting lines
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
            #not utilized atm
    
    cTime = time.time() #gets current time
    fps = 1/(cTime-pTime) #getting frames per second
    pTime = cTime

    #displaying fps on live stream
    #Syntax: cv2.putText(image, text to display, position, font, scale, colour(RGB), thickness)
    cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_COMPLEX, 3,
    (255, 0, 255), 3)


    cv2.imshow("Image", img)
    cv2.waitKey(1)


    






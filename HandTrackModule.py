import cv2
import mediapipe as mp 
import time
import numpy as np 


class handDetector():

    def __init__(self, mode=False, maxHands = 2, modelC=1,detectionCon = 0.5, trackCon = 0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.modelC = modelC
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.modelC, self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils 


    def findHands(self, img, draw=True):
        #converting to rgb 
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.result = self.hands.process(imgRGB)
        #print(results.multi_hand_landmarks)

        if self.result.multi_hand_landmarks:
            for handLms in self.result.multi_hand_landmarks:
                #getting co-ordinates in each id
                #these are decimal values, not pixels
                #multiply by width and height to get pixel
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
                    

        return img       

    def findPosition(self, img, handNo=0, draw=True):

        landMarkList = []
        if self.result.multi_hand_landmarks:
            myHand = self.result.multi_hand_landmarks[handNo]

            for id, lm in enumerate(myHand.landmark):
                        #print(id, lm)
                        h, w, c = img.shape
                        cx, cy = int(lm.x*w), int(lm.y*h)
                        #print(id, cx, cy)
                        landMarkList.append([id, cx, cy])
                        #In Hand Landmark Model, id=0 is wrist, id=4 is thumb_tip
                        #Drawing a circle on the tip of thumb and index finger 
                        if draw:
                            cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
                            #mpHands.HANDCONNECTIONS draws connecting lines
                            if id == 4:
                                cv2.circle(img, (cx, cy), 15, (0, 0, 255), cv2.FILLED)
                            if id == 8:
                                cv2.circle(img, (cx, cy), 15, (0, 0, 255), cv2.FILLED)


        return landMarkList

def main():

    prevTime = 0 #prev time is 0
    currTime = 0 #curr time is 0

    cap = cv2.VideoCapture(0)
    detector = handDetector()

    while True:
        success, img = cap.read()
        img = detector.findHands(img)

        lmList = detector.findPosition(img)
        if len(lmList)!= 0:
            print(lmList[4])
            
        currTime = time.time() #gets current time
        fps = 1/(currTime-prevTime) #getting frames per second
        prevTime = currTime

        #displaying fps on live stream
        #Syntax: cv2.putText(image, text to display, position, font, scale, colour(RGB), thickness)
        cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_COMPLEX, 3,
        (255, 0, 255), 3)


        cv2.imshow("Webcam", img)
        cv2.waitKey(1)

if __name__ == "__main__":
    main()

    




               
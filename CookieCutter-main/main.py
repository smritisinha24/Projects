import os
import cv2
from cvzone import HandTrackingModule, overlayPNG
import numpy as np

folderPath = 'frames'
mylist = os.listdir(folderPath)
graphic = [cv2.imread(f'{folderPath}/{imPath}') for imPath in mylist]
intro = graphic[0];
kill = graphic[1];
winner = graphic[2];

cam = cv2.VideoCapture(0)  

detector = HandTrackingModule.HandDetector(maxHands=1, detectionCon=0.77)

folderPath = 'img'
graphic = [cv2.imread(f'{folderPath}/{imPath}') for imPath in mylist]
sqr_img = graphic[0];
mlsa = graphic[1];

gameOver = False
NotWon = True
while not gameOver:

    ret, frame = cam.read()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    hands = detector.detectHands(gray)
    
    if len(hands) > 0:
        handLandmarks = hands[0]["lmList"]
        
        x, y = handLandmarks[8][1], handLandmarks[8][2]
        
        if y < sqr_img.shape[0]:
            if sqr_img.shape[1] // 2 - 50 < x < sqr_img.shape[1] // 2 + 50:
                gameOver = True
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    continue

if NotWon:
    for i in range(10):
        cv2.imshow("Loss Screen", kill)
        cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    cv2.imshow("Win Screen", winner)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
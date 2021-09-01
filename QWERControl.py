import cv2
import HandTrackingModule as htm
import time
import keyboard

wCam, hCam = 640, 480
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0
detector = htm.handDetector(maxHands=1)

while True:
    #Find hand landmarks
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)

    if len(lmList)!=0:
        #Detect Which Fingers are up
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]
        fingers = detector.fingersUp()
        print(fingers)

        if (fingers[0] == 1):
            print("P key being held")
            keyboard.press('p')
            time.sleep(0.5)
            keyboard.release('p')


        if (fingers[1] == 0):
            print("R key being held")
            keyboard.press('r')
            time.sleep(0.5)
            keyboard.release('r')

        if (fingers[2] == 0):
            print("E key being held")
            keyboard.press('e')
            time.sleep(0.5)
            keyboard.release('e')

        if (fingers[3] == 0):
            print("W key being held")
            keyboard.press('w')
            time.sleep(0.5)
            keyboard.release('w')

        if (fingers[4] == 0):
            print("Q key being held")
            keyboard.press('q')
            time.sleep(0.5)
            keyboard.release('q')


    #Frame rate
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 0), 3)

    # 12. Display
    cv2.imshow("Image", img)
    cv2.waitKey(1)

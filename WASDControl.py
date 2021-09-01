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
            cv2.putText(img, str("SPACE"), (490, 50), cv2.FONT_HERSHEY_PLAIN, 3,
                        (127, 255, 0), 3)
            print("SPACE key being held")
            keyboard.press('space')
            time.sleep(0.5)
            keyboard.release('space')


        if (fingers[1] == 0):
            cv2.putText(img, str("D"), (600, 100), cv2.FONT_HERSHEY_PLAIN, 3,
                        (127, 255, 0), 3)
            print("D key being held")
            keyboard.press('d')
            time.sleep(0.5)
            keyboard.release('d')

        if (fingers[2] == 0):
            cv2.putText(img, str("W"), (600, 150), cv2.FONT_HERSHEY_PLAIN, 3,
                        (127, 255, 0), 3)
            print("W key being held")
            keyboard.press('w')
            time.sleep(0.5)
            keyboard.release('w')

        if (fingers[3] == 0):
            cv2.putText(img, str("A"), (600, 200), cv2.FONT_HERSHEY_PLAIN, 3,
                        (127, 255, 0), 3)
            print("A key being held")
            keyboard.press('a')
            time.sleep(0.5)
            keyboard.release('a')

        if (fingers[4] == 0):
            cv2.putText(img, str("S"), (600, 250), cv2.FONT_HERSHEY_PLAIN, 3,
                        (127, 255, 0), 3)
            print("S key being held")
            keyboard.press('s')
            time.sleep(0.5)
            keyboard.release('s')


    #Frame rate
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 0), 3)

    # 12. Display
    cv2.imshow("Image", img)
    cv2.waitKey(1)

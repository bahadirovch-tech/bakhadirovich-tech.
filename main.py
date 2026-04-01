import cv2
from cvzone.HandTrackingModule import HandDetector
import pyautogui

# Kamerani sozlash
cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=1)

# Ekran o'lchami
screen_width, screen_height = pyautogui.size()

print("AI Mouse (cvzone versiyasi) ishga tushdi...")

while True:
    success, img = cap.read()
    if not success:
        break
        
    img = cv2.flip(img, 1) # Ko'zgudek aks ettirish
    
    # Qo'lni topish
    hands, img = detector.findHands(img) 

    if hands:
        # Birinchi qo'lni olamiz
        hand1 = hands[0]
        lmList = hand1["lmList"] # 21 ta nuqta koordinatasi
        
        # Ko'rsatkich barmog'i uchi (8-nuqta)
        index_finger_x, index_finger_y = lmList[8][0], lmList[8][1]

        # Kameradagi koordinatani ekranga moslash
        # (Kamera odatda 640x480 bo'ladi)
        mouse_x = (screen_width / 640) * index_finger_x
        mouse_y = (screen_height / 480) * index_finger_y

        # Sichqonchani harakatlantirish
        pyautogui.moveTo(mouse_x, mouse_y)

    # Natijani ko'rsatish
    cv2.imshow("TUIT AI Mouse", img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()














import cv2

import pyautogui  # إذا عندك autopygui نفس الفكرة تقريباً

import datetime


cwd = os.path.dirname(os.path.abspath(__file__))




def main():
    # فتح الكاميرا
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("لا يمكن فتح الكاميرا")
        return

    while True:
        
        ret, frame = cap.read()
        
        if not ret:
            print("لم أستطع قراءة الفيديو")
            break
        
        # كتابة رسالة على الفيديو
        
        text = "اضغط على الحرف P لالتقاط صورة للشاشة"
        
        cv2.putText(frame, text, (20, 40), cv2.FONT_HERSHEY_SIMPLEX,
                    0.8, (0, 255, 0), 2, cv2.LINE_AA)
        
        # عرض الفيديو
        
        cv2.imshow("نافذة الكاميرا", frame)
        
        
        # التقاط لوحة المفاتيح
        
        key = cv2.waitKey(1) & 0xFF
        
        if key == ord('q'):  # للخروج بالضغط على q
            
            break
            
        elif key == ord('p'):
            
            # التقاط صورة للشاشة
            
            screenshot = pyautogui.screenshot()
            
            filename = os.path.join(cwd, f"screenshot_{datetime.datetime.now().strftime('%Y_%m_%d__%H_%M_%S')}.png")
            
            screenshot.save(filename)
            
            print(f"تم حفظ لقطة الشاشة: {filename}")
            

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    
    main()
    
    














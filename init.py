import cv2

captura = cv2.VideoCapture(0)

while(not cv2.waitKey(20) & 0xFF == ord('q')):
    ret, frame = captura.read()
    cv2.imshow("Video", frame)
   
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

captura.release()
cv2.destroyAllWindows()
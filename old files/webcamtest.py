import numpy as np
import cv2
from compare2set import compare2set

setcode = 'MM3'


compareset = compare2set(setcode)

cap = cv2.VideoCapture(0)
fin = False
while(not fin):
    ret, frame = cap.read()

    cv2.imshow('frame',frame)
    inp = cv2.waitKey(1) & 0xFF
    if inp == ord('q'):
        fin = True
    if inp == ord('c'):
        compareset.compareimg(frame)

cap.release()
cv2.destroyAllWindows()
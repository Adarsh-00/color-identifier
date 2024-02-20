import cv2
import numpy as np

def indentify_color(event, x, y, flag, param) :
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]

        colorImg = np.zeros((150,250,3), np.uint8)
        colorImg[:] = [blue, green, red]
        font = cv2.FONT_HERSHEY_SIMPLEX
        color = "RGB(" + str(red) + ", " + str(green) + ", "+ str(blue) + ")"
        cv2.putText(colorImg, color, (20,40), font, 0.6, (70, 70, 70), 2)
        cv2.imshow("color", colorImg)



img = cv2.imread("colors.jpg") #put image name here
cv2.imshow("image", img)
cv2.setMouseCallback("image", indentify_color)

cv2.waitKey(0)
cv2.destroyAllWindows()
#basic drawing functions of opencv

import cv2, numpy

cv2.namedWindow("drawings")
background = cv2.imread("./img/SF_copy2.jpeg") #more like a canvas where our little cute things will go on, then just put this on the window frame

cv2.line(background, (50,50), (400,400),(255,0,0), 3)
cv2.rectangle(background, (500, 20), (580, 100), (0,255,0), 2)
cv2.rectangle(background, (100,300), (150,360), (0,0,255), -1)
cv2.circle(background, (500,300), 40, (255,255,0), -1)

pts = numpy.array([[300,300],[300,340],[350,320]], numpy.int32)
cv2.polylines(background, [pts], True, (0,255,255), 2)
cv2.putText(background, "Background canvas of SF Bridg", (350,420),cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)

cv2.imshow("drawings", background)
cv2.waitKey(0)
print("----saving image----")
cv2.imwrite("./img/SF_drawings.jpeg", background, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
print("image saved!")
cv2.destroyAllWindows()


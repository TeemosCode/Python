import cv2, os
print("Basic foundations of opencv window frame")
cv2.namedWindow("OpenCV window Frame", cv2.WINDOW_KEEPRATIO)

input("press enter to destroy (close) opencv window")
cv2.destroyWindow("OpenCV window Frame")

img = cv2.imread("./img/SF.jpg", 0) # 1: colorful, 0: gray, -1: original

cv2.imshow("OpenCV window Frame", img)


cv2.waitKey(1000) # infinity time: 0, until user clicks any buttons on the keyboard while on the processed image


print('======')


cv2.namedWindow("Frame1")
cv2.namedWindow("Frame2")

image1 = cv2.imread("./img/SF.jpg", 1)
image2 = cv2.imread("./img/SF.jpg", 0)

cv2.imshow("Frame1",image1)
cv2.imshow("Frame2", image2)

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("./img/SF_copy1.jpg", image1)
cv2.imwrite("./img/SF_copy2.jpeg", image2, [int(cv2.IMWRITE_JPEG_QUALITY), 50])
print("Image saved")
print("Opening image...")

os.system("open ./img/SF_copy1.jpg")
os.system("open ./img/SF_copy2.jpeg")
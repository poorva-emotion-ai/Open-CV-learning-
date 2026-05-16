import cv2

img1 = cv2.imread("panda.jpg")
img2 = cv2.imread("rabbit.jpg")

# Resize second image to match first image
img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

bitAnd = cv2.bitwise_and(img1, img2)
bitOr = cv2.bitwise_or(img1, img2)
bitxor = cv2.bitwise_xor(img1, img2)
bitNot = cv2.bitwise_not(img1)

cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.imshow("bitAnd", bitAnd)
cv2.imshow("bitOr", bitOr)
cv2.imshow("bitXor", bitxor)
cv2.imshow("bitNot", bitNot)

cv2.waitKey(0)
cv2.destroyAllWindows()


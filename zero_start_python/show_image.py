import cv2

img = cv2.imread('block.jpg')
height = img.shape[0]
width = img.shape[1]
resized_img = cv2.resize(img, (int(width/2), int(height/2)))
cv2.imwrite('resized_block.jpg', resized_img)

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite('gray_block.jpg', gray_img)

canny_img = cv2.Canny(img, 50, 100)
cv2.imwrite('canny_block.jpg', canny_img)

cv2.imshow('block', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

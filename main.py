import cv2
#trained dataset
train=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


#read image'
img=cv2.imread('images/multi.jpg')

#convert into grayscale
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces=train.detectMultiScale(gray)
for x,y,w,h in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(225,255,0),2)
print(faces)
cv2.imshow('mani',img)
# cv2.imshow('gray',gray)
cv2.waitKey()
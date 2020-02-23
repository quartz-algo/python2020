#IMAGE-PROCESSING ASSIGNMENT TO DETECT CARS IN A GIVEN VIDEO
import cv2

car_cascade = cv2.CascadeClassifier(r'cars.xml')

vid = cv2.VideoCapture(r'video1.avi')
while True:
    check,frame = vid.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)


    cars = car_cascade.detectMultiScale(gray,scaleFactor=1.05,minNeighbors=5)

    print(cars)

    for x,y,w,h in cars:
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,0),3)

    cv2.imshow('GRAY VIDEO',frame)
    cv2.waitKey(10)
cv2.destroyAllWindows()
vid.release()
import cv2
student_id=input("enter your id")

#starting video cam
vid_cam = cv2.VideoCapture(0)

#detecting face using haarcascade
face_detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#initila count
count = 0

#looping
while(True):

    # capture image from video
    _,img_frame = vid_cam.read()

    #now converting image into gray scale image
    gray =cv2.cvtColor(img_frame,cv2.COLOR_BGR2GRAY)

    #detecting face rectangle in frame
    face = face_detector.detectMultiScale(gray,1.3,6)

    #loop for each face
    for(x,y,w,h) in face:

        #croping image frame into face rectangle
        cv2.rectangle(img_frame,(x,y),(x+w,y+h),(255,0,0),2)
        img=gray[y:y+h,x:x+w]
        count +=1

        #saving the capture face rectangle
        cv2.imwrite("C:\\Users\\intex\\PycharmProjects\\final project\\venv\\samples\\users." +'id['+ str(student_id)+']'+str(count)+".jpg",img)


        #create a on sceen counter  to show no of frae captured
        cv2.putText(img_frame, str(count), (30, 50), cv2.FONT_HERSHEY_PLAIN, 1.5, (255, 0, 0), 1)
        #cv2.putText(img_frame, str(student_id), (40, 40), cv2.FONT_HERSHEY_PLAIN, 1.5, (255, 0, 0), 1)


        #show frame with ractangle on face
        cv2.imshow("capturing frame",img_frame)


    if count== 100:
        print("capture complete")
        break
    elif cv2.waitKey(1)==13:
        break

#stop vedio
vid_cam.release()

#close all win
cv2.destroyAllWindows()



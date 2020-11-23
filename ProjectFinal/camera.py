import cv2
import numpy as np
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
scale_percent = 60 # percent of original size
class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)   #feed #cv2 bit array me convert krta h

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, image = self.video.read()
        width = int(image.shape[1] * scale_percent / 100)  ##change the width he acc to ourselves
        height = int(image.shape[0] * scale_percent / 100)
        dim = (width, height)
        resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
        ret, jpeg = cv2.imencode('.jpg', resized)
        return jpeg.tobytes()
    def get_frame_bw(self):
        success, image = self.video.read()
        width = int(image.shape[1] * scale_percent / 100)
        height = int(image.shape[0] * scale_percent / 100)
        dim = (width, height)
        resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
        gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY) #color chnage
        ret, jpeg = cv2.imencode('.jpg', gray)
        return jpeg.tobytes()
    def get_frame_hr(self):
        success, image = self.video.read()
        #scaling acc to the app
        width = int(image.shape[1] * scale_percent / 100)
        height = int(image.shape[0] * scale_percent / 100)
        dim = (width, height)
        img = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x,y,w,h) in faces:  #faces detect krk eeyes ko detect kr rha
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)  #last vala 2 uski thickness rect ki
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]

            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (ex,ey,ew,eh) in eyes:
                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

        ret, jpeg = cv2.imencode('.jpg', img)
        return jpeg.tobytes()
    def get_frame_rm(self):
        success, image =self.video.read()
        width = int(image.shape[1] * scale_percent / 100)
        height = int(image.shape[0] * scale_percent / 100)
        dim = (width, height)
        img = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        lower_red = np.array([-10,125,84]) #range of values jha tk chahiye red
        upper_red = np.array([10,255,255])##yha tk allow krdega

        mask = cv2.inRange(hsv, lower_red, upper_red)
        res = cv2.bitwise_and(img,img, mask= mask) ##baki sabko zero krdiya
        ret, jpeg = cv2.imencode('.jpg', res)
        return jpeg.tobytes()

    def get_frame_bm(self):
        success, image =self.video.read()
        width = int(image.shape[1] * scale_percent / 100)
        height = int(image.shape[0] * scale_percent / 100)
        dim = (width, height)
        img = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        lower_blue = np.array([88,125,84])
        upper_blue = np.array([135,255,255])

        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        res = cv2.bitwise_and(img,img, mask= mask)
        ret, jpeg = cv2.imencode('.jpg', res)
        return jpeg.tobytes()
    def get_frame_gm(self):
        success, image =self.video.read()
        width = int(image.shape[1] * scale_percent / 100)
        height = int(image.shape[0] * scale_percent / 100)
        dim = (width, height)
        img = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        lower_green = np.array([37,125,84])
        upper_green = np.array([75,255,255])

        mask = cv2.inRange(hsv, lower_green, upper_green)
        res = cv2.bitwise_and(img,img, mask= mask)
        ret, jpeg = cv2.imencode('.jpg', res)
        return jpeg.tobytes()

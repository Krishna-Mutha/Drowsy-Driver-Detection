import cv2 as cv
import imutils
from imutils import face_utils
import dlib
from scipy.spatial import distance
from pygame import mixer
import sys,os

def eyeAspectRatio(eye):
    vertical_1=distance.euclidean(eye[1],eye[5])
    vertical_2=distance.euclidean(eye[2],eye[4])
    horizontal=distance.euclidean(eye[0],eye[3])
    EAR=(vertical_1*vertical_2)/(2.0*horizontal)
    return EAR

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

ALARM_SOUND=resource_path("music.wav")
LANDMARK_SET=resource_path("shape_predictor_68_face_landmarks.dat")
CAMERA_ID=0
THRESH=0.85
mixer.init()
mixer.music.load(ALARM_SOUND)
flag=0
frame_thresh=20
while True:
    try:
        cam_id=int(input("Enter Camera ID to use (0 if only one camera is present): "))
        CAMERA_ID=cam_id
        break
    except:
        continue
face_detector=dlib.get_frontal_face_detector()
face_landmarks=dlib.shape_predictor(LANDMARK_SET)
(lstart,lend)=face_utils.FACIAL_LANDMARKS_68_IDXS['left_eye']
(rstart,rend)=face_utils.FACIAL_LANDMARKS_68_IDXS['right_eye']
cap=cv.VideoCapture(CAMERA_ID)
while True:
    ret,frame=cap.read()
    if ret:
        frame=imutils.resize(frame,width=450)
        cv.putText(frame,"Press Q to Close",(frame.shape[1]-125,frame.shape[0]-25),cv.FONT_HERSHEY_SIMPLEX,0.4,(0,255,0),1)
        gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
        faces=face_detector(gray,0)
        for face in faces:
            shape=face_landmarks(gray,face)
            shape=face_utils.shape_to_np(shape)
            leftEye=shape[lstart:lend]
            rightEye=shape[rstart:rend]
            L_EAR=eyeAspectRatio(leftEye)
            R_EAR=eyeAspectRatio(rightEye)
            EAR=(L_EAR+R_EAR)/2.0
            leftHull=cv.convexHull(leftEye)
            rightHull=cv.convexHull(rightEye)
            cv.drawContours(frame,[leftHull],-1,(0,255,0),1)
            cv.drawContours(frame,[rightHull],-1,(0,255,0),1)
            print(EAR)
            if EAR<THRESH:
                flag+=1
                if(flag>=frame_thresh):
                    cv.putText(frame,"****ALERT****",(10,30),cv.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)
                    print('WARNING')
                    if(not(mixer.music.get_busy())):
                        mixer.music.play()
                        print(f'Playing {ALARM_SOUND}')
            else:
                flag=0
                mixer.music.stop()
    else:
        break
    cv.imshow('Frame',frame)
    if cv.waitKey(1) & 0xFF==ord("q"):
        print("Program Closed")
        break
cv.destroyAllWindows
cap.release()
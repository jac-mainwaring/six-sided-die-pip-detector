# list of imported packages
import cv2 # imports opencv
import numpy as np # this makes it easier to call upon numpy
from collections import deque



max_thres = 200 # diffrent lighting, camera distance
min_thres = 10 # these are how we adjust the settings for  
area = 100 #      and angle or focus
min_inertia_ratio = 0.5 #inertia
min_circularity = 0.3 #circularity


cam = cv2.VideoCapture(1) # this imports the ability to access the camera for to be called and used by the rest of the code
                          # the number sets it to the camera in use, by defult it will usualy be 0 but if you have other inputs it might read you might need to change it
                          # i for example have a capture card so sometimes i might need to change it to one as itll read that as an input source
cam.set(15, -4)# this is used as a reference for the exposure of the camera with the 15 referencing it and the -4 setting it


display = deque([0,0], maxlen=10)# used in lists to handle the tracking of how many pips pips
reading = deque([0,0], maxlen=10)
count = 0 # counter for the fps


while True:
    ret, frame = cam.read() #frame is what will be used to represent a frame in the video feed 

    params = cv2.SimpleBlobDetector_Params () #these are the parameters for the video filter and the blobdetector
   
    params.maxThreshold = max_thres #https://docs.opencv.org/4.x/d8/da7/structcv_1_1SimpleBlobDetector_1_1Params.html 
    params.minThreshold = min_thres #the link above is a list of the parameters by opencv themselves
    params.minArea = area
    params.minInertiaRatio = min_inertia_ratio
    params.minCircularity = min_circularity
    params.filterByArea = True
    params.filterByInertia = True
    params.filterByCircularity = True

    detector = cv2.SimpleBlobDetector_create(params) # makes an object for the blob detector 

    point = detector.detect(frame) # this is for a list that contains the detected blobs

    frame_with_point = cv2.drawKeypoints(frame, point, np.array([]), (0, 0, 255),
                                        cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS) #this is where we shall draw the points onto the frame we are using.

    cv2.imshow("pip detector", frame_with_point) #displays frames with the points added 

    if count % 10 == 0:  # enter this every 10 frames
        read = len(point) # reading is what counts the number of pips
        reading.append(read) #this should let us record the reading given

        if reading[-1] == reading[-2] == reading[-3]:    #this tests if the reading is valid by checking the reading three times
            display.append(reading[-1])                   

        # this checks for the latest reading and if it is a diffrent reading than the last while also being above 0 it will print it
        if display[-1] != display[-2] and display[-1] != 0:
            file1 = open("Data.txt","a")# this will be used to open a txt file to edit
            msg = f"{display[-1]}\n"
            print(msg)
            file1.write(msg)
            file1.close()
 
    count += 1
 
    if cv2.waitKey(1) & 0xff == 27:                          # press [Esc] to close
        break

cv2.destroyAllWindows()

import cv2, time, pandas
from datetime import datetime

first_frame = None
status_list = [None, None]
times = []
#DataFrame to store the time values during which object detection and movement appears
df = pandas.DataFrame(columns=["Start","End"])

#Create a VideoCapture object to record using web cam
video = cv2.VideoCapture(0)

while True:
    check, frame = video.read()
    #Status at the beginning of the recording is zero as the object is not visible
    status = 0
    #Convert the frame color to gray scale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #Convert the gray scale to GaussianBlur
    gray = cv2.GaussianBlur(gray,(21,21),0)

    #This used to store the first image/frame of the video
    if first_frame is None:
        first_frame = gray
        continue

    #Calculates the difference between the first frame and other frames
    delta_frame = cv2.absdiff(first_frame, gray)

    #Provides a threshold value, such that it will convert the difference value with less than 30 to black.
    #If the difference is greater than 30 it will convert those pixels to white
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)

    #Define contour area. Basically, add the borders
    (cnts,_) = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    #Removes noises and shadows. Basically, it will keep only that part white, which has area greater than 1000 pixels
    for contour in cnts:
        if cv2.contourArea(contour) < 10000:
            continue
        status = 1     #Change in status when the object is being detected
        #Creates a rectangular box around the object in the box
        (x,y,w,h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 3)
    status_list.append(status)      #List of status for every frame

    status_list = status_list[-2:]

    #Record date time in a list when change occurs
    if status_list[-1] == 1 and status_list[-2] == 0:
        times.append(datetime.now())
    if status_list[-1] == 0 and status_list[-2] == 1:
        times.append(datetime.now())

    # cv2.imshow('frame', frame)
    # cv2.imshow('Capturing', gray)
    # cv2.imshow('delta', delta_frame)
    # cv2.imshow('thresh', thresh_frame)
    cv2.imshow('Gray frame', gray)
    cv2.imshow('Delta frame', delta_frame)
    cv2.imshow('Threshold frame',thresh_frame)
    cv2.imshow('color frame', frame)

    #Frame will change in 1 millisecond
    key = cv2.waitKey(1)

    #This will break the loop, once the user process 'q'
    if key == ord('q'):
        if status==1:
            times.append(datetime.now())
        break

print(status_list)
print(times)

for i in range(0, len(times), 2):
    #Store time values in a DataFrame
    df = df.append({"Start":times[i], "End":times[i+1]}, ignore_index=True)

df.to_csv("Times.csv")

video.release()
#This will close all the windows
cv2.destroyAllWindows()
import cv2
import time
import glob
import os
from threading import Thread
from emailing import send_emails
# VideoCapture() takes arg 0 for first camera and 1 for the webcam or second camera.
video = cv2.VideoCapture(0)
time.sleep(1)

first_frame = None
status_list = []
count=1

# Clear all the captured images
def clear_folder():
    print("clear_folder function started")
    images = glob.glob("images/*.png")
    for image in images:
        os.remove(image)
    print("clear_folder function ended")

while True:
    status = 0
    check,frame = video.read()

    # Converted the image to gray scale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Blurred the background
    gray_frame_gau = cv2.GaussianBlur(gray_frame,(21,21),0)

    # Here we assign the value of the very first frame from which we are going to compare.
    if first_frame is None:
        first_frame = gray_frame_gau

    # Checks the difference between the first frame and the current frame.
    delta_frame = cv2.absdiff(first_frame, gray_frame_gau)

    # If pixels intensity is greater than the set threshold,than the value is set to 255, else set to 0(black).
    thresh_frame = cv2.threshold(delta_frame,20,255, cv2.THRESH_BINARY)[1]
    dil_frame = cv2.dilate(thresh_frame , None, iterations = 2)

    # Creating an image with contour around the white areas.
    contours , check = cv2.findContours(dil_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        if cv2.contourArea(contour) < 5000:
            continue
        x,y,w,h = cv2.boundingRect(contour)
        # Coordinates of the rectangle,colour,width as an arg of the rectangle.
        rectangle = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
        if rectangle.any():
            status = 1
            cv2.imwrite(f"images/{count}.png", frame)
            count = count + 1
            all_images = glob.glob("images/*.png")
            index = int(len(all_images) /2) # Picking the middle image
            image_with_object = all_images[index]

    status_list.append(status)
    status_list = status_list[-2:]
    # The mail is sent when the condition is met.
    if status_list[0] == 1 and status_list[1] ==0:
        # send_emails(image_with_object) {since there was a lag while execution so instead of this we are using threads}
        email_thread = Thread(target = send_emails,args = (image_with_object , ))
        email_thread.daemon = True
        clean_thread = Thread(target= clear_folder)
        clean_thread.daemon = True

        email_thread.start()

    print(status_list)

    cv2.imshow("Video", frame)
    key = cv2.waitKey(1)
    if key == ord("a"):
        break

video.release()

clear_folder()
import time
import glob
import os
from threading import Thread
from modules.send_email import send_email
import cv2


# Start capturing video with the main camera
video = cv2.VideoCapture(2)
time.sleep(1)

first_frame = None
status_list = []
count = 1


def clean_dir():
    images = glob.glob("./images/*.png")
    for image in images:
        os.remove(image)


# Record a video
while True:
    status = 0
    # Get data from the camera
    check, frame = video.read()
    # Convert the frame to a grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Add some blur to the gray frame
    gray_frame_gau = cv2.GaussianBlur(gray_frame, (21, 21), 0)
    # Save the first frame from the video
    if first_frame is None:
        first_frame = gray_frame_gau
    # Get a new frame from the difference of the first and the current gray blurred frame
    delta_frame = cv2.absdiff(first_frame, gray_frame_gau)
    # Convert the frame to only black or white colors
    thresh_frame = cv2.threshold(delta_frame, 40, 255, cv2.THRESH_BINARY)[1]
    # Delete some noise from the frame
    dil_frame = cv2.dilate(thresh_frame, None, iterations=2)
    # Display the frame (because of the loop it will be displayed as a video)
    cv2.imshow("My video", dil_frame)
    # Get contours of the objects
    contours, check = cv2.findContours(dil_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        # If it is a "small object" perhaps is a false positive
        if cv2.contourArea(contour) < 5000:
            continue
        # Get the size of the Rectangle for the cotour object
        x, y, w, h = cv2.boundingRect(contour)
        # Draw rectangle around a object in the frame
        rectangle = cv2.rectangle(
            frame, 
            pt1=(x, y), 
            pt2=(x + w, y + h), 
            color=(0, 255, 0), 
            thickness=3
        )
        # Set status to "True" when a object is on the camera
        if rectangle.any():
            status = 1
            # Save an image every time an object is detected
            cv2.imwrite(f"./images/{count}.png", frame)
            count += 1
            # Get a list of images path 
            all_images = glob.glob("./images/*.png")
            # Save the middle image
            index = len(all_images) // 2
            image_with_object = all_images[index]

    # Get last 2 elements to know when there's a change on the camera
    status_list.append(status)
    status_list = status_list[-2:]
    # Send email when the object leaves the field of view
    if status_list[0] == 1 and status_list[1] == 0:
        # Creating threads for functions
        email_thread = Thread(target=send_email, args=(image_with_object, ))
        email_thread.daemon = True
        clean_thread = Thread(target=clean_dir)
        clean_thread.daemon = True
        # Starting thread
        email_thread.start()
        clean_thread.start()
        
    cv2.imshow("Video", frame)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break

video.release()

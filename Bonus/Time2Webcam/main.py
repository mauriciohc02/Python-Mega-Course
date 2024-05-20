from datetime import datetime
import cv2
import streamlit as st


# Webpage configuration
st.set_page_config(
    page_title="Time to Webcam", 
    page_icon=":camera:", # https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
    layout="centered"
)

# Set a title
st.title("Motion Detector")
# Set a button
start = st.button("Start Camera")

if start:
    # Initialize the space for the image
    image = st.image([])
    # Start capturing video with the main camera
    camera = cv2.VideoCapture(0)

    while True:
        # Get data from the camera
        check, frame = camera.read()
        # Change the color format
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # Get timestamp
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        day = now.strftime("%A")
        # Add day as text to the current frame
        cv2.putText(
            img=frame,
            text=f"{day}",
            org=(30, 80),
            fontFace=cv2.FONT_HERSHEY_PLAIN,
            fontScale=2, 
            color=(255, 255, 255),
            thickness=2,
            lineType=cv2.LINE_AA
        )
        # Add current time as text to the current frame
        cv2.putText(
            img=frame,
            text=f"{current_time}",
            org=(30, 140),
            fontFace=cv2.FONT_HERSHEY_PLAIN,
            fontScale=2, 
            color=(255, 0, 0),
            thickness=2,
            lineType=cv2.LINE_AA
        )
        # Update the image
        image.image(frame)

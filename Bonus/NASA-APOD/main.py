import os
from datetime import datetime
import streamlit as st
import requests


# Get API_KEY from an Env Variable
API_KEY = os.getenv("NASA_API_KEY") # Get your key from https://api.nasa.gov/
# URL for the request
url = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"

# Make request
response = requests.get(url=url)
# Get a dictionary with data
content = response.json()

# Extract Title, Image URL and explanation
title = content["title"]
image_url = content["hdurl"]
explanation = content["explanation"]

# Download Image
today = datetime.now().strftime("%Y-%m-%d")
image_filepath = f"./images/{today}.jpg"
image_response = requests.get(url=image_url)
# Save Image
with open(image_filepath, "wb") as file:
    file.write(image_response.content)

# Webpage configuration
st.set_page_config(
    page_title="NASA's APOD",
    page_icon=":stars:", # https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
    layout="centered"
)

# Show NASA's Astronomy Picture of the Day (APOD)
st.title(title)
st.image(image_filepath)
st.write(explanation)

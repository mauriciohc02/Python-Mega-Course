import streamlit as st
import pandas as pd


def show_project(row) -> None:
    """
    Show a Project with its data from the row
    """
    st.header(row["title"])
    st.write(row["description"])
    st.image(f"images/{row['image']}")
    st.write(f"[Source code]({row['url']})")

# Webpage configuration
st.set_page_config(
    page_title="My Portfolio", 
    page_icon=":open_file_folder:", # https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
    layout="centered"
)

col1, col2 = st.columns(2)
# Add my photo to the left column
with col1:
    st.image(image="images/photo.png")
# Add a title and text to the right column
with col2:
    st.title("Mauricio Hernandez Cepeda")
    aboutMe = """
        Hi, I am Mauricio! A highly motivated and skilled IT Engineering student with experience in Docker, Python, Linux and CCNA certified. Strong problem-solving skills and teamwork abilities. Spanish native speaker and proficient in English (B2)
    """
    st.info(aboutMe)

# Show a description as text
description = """
    Below you can find some of the apps I have built in Python. Feel free to contact me!
"""
st.write(description)

# Create columns with different size
col3, empty_col, col4 = st. columns([1.5, 0.5, 1.5])
# Read data from the .csv
df = pd.read_csv("db/data.csv", sep=";")
# Show first 10 projects
with col3:
    for index, row in df[:10].iterrows():
        show_project(row=row)
# Show last 10 projects
with col4:
    for index, row in df[10:].iterrows():
        show_project(row=row)


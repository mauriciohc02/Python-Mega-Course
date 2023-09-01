import streamlit as st
import pandas as pd


def show_employee(row) -> None:
    """
    Show a Employee with its data from the row
    """
    first_name, last_name = row['first name'].title(), row['last name'].title()
    st.subheader(f"{first_name} {last_name}")
    st.write(f"{row['role']}")
    st.image(f"images/{row['image']}")

# Webpage configuration
st.set_page_config(
    page_title="My Company",
    page_icon=":classical_building:", # https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
    layout="wide"
)
# Show text in different formats
st.title("The Best Company")
description = """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""
st.write(description)
st.subheader("Our Team")
# Create columns with the same size
col1, col2, col3 = st.columns(3)
# Read data from the .csv
df = pd.read_csv("db/data.csv", sep=",")
# Show first 4 employees
with col1:
    for index, row in df[:4].iterrows():
        show_employee(row=row)
# Show the next 4 employees
with col2:
    for index, row in df[4:8].iterrows():
        show_employee(row=row)
# Show last 4 employees
with col3:
    for index, row in df[8:].iterrows():
        show_employee(row=row)
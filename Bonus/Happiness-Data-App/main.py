import streamlit as st
import plotly.express as px
import pandas as pd


def get_data(x, y):
    """
    Read csv and return data for each axis
    """
    x = x.lower().replace(" ", "_")
    y = y.lower().replace(" ", "_")
    df = pd.read_csv("./db/happy.csv")

    return df[x], df[y]


# Webpage configuration
st.set_page_config(
    page_title="Happiness Data App", 
    page_icon=":smile:", # https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
    layout="centered"
)
# Options
options = (
    "Happiness",
    "GDP",
    "Social Support",
    "Life Expectancy",
    "Freedom to Make Life Choices",
    "Generosity",
    "Corruption"
)

# Set a title
st.title("In Search for Happiness")
# Define parameteres for the user
option_x = st.selectbox("Select the data for the X-axis", options)
option_y = st.selectbox("Select the data for the Y-axis", options)
# Set a subtitle
st.subheader(f"{option_x} and {option_y}")
# Get data for the Plot
x, y = get_data(option_x, option_y)
# Create Scatter Plot
figure = px.scatter(x=x, y=y, labels={"x": option_x, "y": option_y})
# Show Plot
st.plotly_chart(figure)

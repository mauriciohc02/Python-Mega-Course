import glob
from pathlib import Path
import streamlit as st
import plotly.express as px
from nltk.sentiment import SentimentIntensityAnalyzer


# Webpage configuration
st.set_page_config(
    page_title="Mood Analyzer", 
    page_icon=":smile:", # https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
    layout="centered"
)

# Instance the analyzer
analyzer = SentimentIntensityAnalyzer()
# Get a list of filepaths
diary = glob.glob("./diary/*.txt")
diary = sorted(diary)
# Initialize statistics and dates lists
positivity = list()
negativity = list()
dates = list()

for filepath in diary:
    # Extract the filename and add it to the list
    date = Path(filepath).stem # os.path.basename(filepath)
    dates.append(date)
    # Open current file
    with open(filepath, "r") as file:
        day = file.read()
    # Get scores from the Sentimental Analyzer and add it to the list
    day_stats = analyzer.polarity_scores(day)
    positivity.append(day_stats["pos"])
    negativity.append(day_stats["neg"])


# Set a title
st.title("Mood Analyzer")

# Set a subtitle
st.subheader("Positivity")
# Create Linear Plot
figure_pos = px.line(x=dates, y=positivity, labels={"x": "Date", "y": "Positivity"})
# Show Plot
st.plotly_chart(figure_pos)

# Set a subtitle
st.subheader("Negativity")
# Create Linear Plot
figure_neg = px.line(x=dates, y=negativity, labels={"x": "Date", "y": "Negativity"})
# Show Plot
st.plotly_chart(figure_neg)

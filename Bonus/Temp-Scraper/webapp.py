import streamlit as st
import plotly.express as px
import sqlite3


connection = sqlite3.connect("./db/data")
cursor = connection.cursor()

cursor.execute("SELECT date FROM temperatures;")
dates = cursor.fetchall()
dates = [item[0] for item in dates]

cursor.execute("SELECT temperature FROM temperatures;")
temperatures = cursor.fetchall()
temperatures = [item[0] for item in temperatures]

figure = px.line(
    x=dates,
    y=temperatures,
    labels={"x": "Date", "y": "Temperature (C)"}
)

st.plotly_chart(figure)

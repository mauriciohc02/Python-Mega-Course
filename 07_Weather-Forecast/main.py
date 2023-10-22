from modules.backend import get_data
import streamlit as st
import plotly.express as px


# Webpage configuration
st.set_page_config(
    page_title="Weather App", 
    page_icon=":sun_small_cloud:", # https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
    layout="centered"
)

# Set a title
st.title("Weather Forecast for the Next Days")
# Define parameteres for the user
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of forecasted days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
# Set a subtitle
st.subheader(f"{option} for the next {days} days in {place}")

# Condition for handling an empty place parameter
if place:
    # Handle Non Exisitng Place Error
    try:
        # Get the temperature/sky data
        data = get_data(place, days)
    except:
        # Show Error message
        st.error("Uh-Oh! You just typed a non existing place, try again!", icon="🚨")
    else:
        # Execute if there's no exception
        if option == "Temperature":
            # Create a list with temperatures values through list comprehension
            temperatures = [float(temp_dict["main"]["temp"] / 10) for temp_dict in data]
            # Create a list with dates through list comprehension
            dates = [dates_dict["dt_txt"] for dates_dict in data]
            # Create Linear Plot
            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
            # Show Plot
            st.plotly_chart(figure)
        elif option == "Sky":
            # Create a list of paths about sky conditions in lowercase through list comprehension
            sky_conditions = [f"./images/{sky_dict['weather'][0]['main'].lower()}.png" for sky_dict in data]
            # Show images
            j = 0
            for i in range(days):
                weather_cols = st.columns(8)
                for col in weather_cols:
                    with col:
                        st.image(sky_conditions[j])
                    j += 1

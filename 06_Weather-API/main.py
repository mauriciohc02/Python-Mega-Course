from flask import Flask, render_template
import pandas as pd


app = Flask(__name__)
data_directory = "data"
# Read the stations.txt file
stations_filename = f"./{data_directory}/stations.txt"
stations = pd.read_csv(stations_filename, skiprows=17)
# Get only a few columns
stations = stations[[
    "STAID",
    "STANAME                                 ",
]]


@app.route("/")
def home():
    # Render HTML and pass a variable
    return render_template("home.html", stations=stations.to_html())


@app.route("/api/v1/<station>/<date>")
def specific_date(station, date):
    # Save file as "./data_small/TG_STAID000010.txt" for example
    filename = f"./{data_directory}/TG_STAID{str(station).zfill(6)}.txt"
    # Read file, skip first 20 rows and parse date to a date format
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    # Get real temperature based on the date
    temperature = df.loc[df["    DATE"] == date]["   TG"].squeeze() / 10
    
    return {
        "station": station,
        "date": date,
        "temperature": temperature
    }


@app.route("/api/v1/<station>")
def all_data(station):
    # Save file as "./data_small/TG_STAID000010.txt" for example
    filename = f"./{data_directory}/TG_STAID{str(station).zfill(6)}.txt"
    # Read file, skip first 20 rows and parse date to a date format
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    # From DataFrame to Dictionary by row
    result = df.to_dict(orient="records")

    return result


@app.route("/api/v1/yearly/<station>/<year>")
def yearly(station, year):
    # Save file as "./data_small/TG_STAID000010.txt" for example
    filename = f"./{data_directory}/TG_STAID{str(station).zfill(6)}.txt"
    # Read file, skip first 20 rows and parse date to a date format
    df = pd.read_csv(filename, skiprows=20)
    # Convert date integer to string
    df["    DATE"] = df["    DATE"].astype(str)
    # Get rows which start with the particular year
    result = df[df["    DATE"].str.startswith(str(year))]
    # From DataFrame to Dictionary by row
    result = result.to_dict(orient="records")

    return result




if __name__ == "__main__":
    app.run(debug=True, port=5000)

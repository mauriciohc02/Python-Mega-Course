from typing import Any
import sqlite3
from modules.send_email import send_email
import requests
import selectorlib


URL: str = "http://programmer100.pythonanywhere.com/tours/"
connection = sqlite3.connect("./db/data")


def scrape(url: str) -> str:
    """
    Scrape the page source from the URL
    """
    response = requests.get(url)
    source = response.text
    
    return source


def extract(source: str) -> Any:
    """
    Extract the data based on .yaml file
    """
    extractor = selectorlib.Extractor.from_yaml_file("./files/extract.yaml")
    value = extractor.extract(source)["tours"]
    
    return value


def store(extracted: Any) -> None:
    """
    Store data in a .db file
    """
    row = extracted.split(",")
    row = [item.strip() for item in row]
    cursor = connection.cursor()
    cursor.execute("INSERT INTO events VALUES(?,?,?);", row)
    connection.commit()


def read(extracted: Any) -> list[Any]:
    """
    Read data from a .db file
    """
    row = extracted.split(",")
    row = [item.strip() for item in row]
    band, city, date = row
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM events WHERE band=? AND city=? AND date=?;", (band, city, date))
    rows = cursor.fetchall()

    return rows


if __name__ == "__main__":
    scraped: str = scrape(url=URL)
    extracted: Any = extract(source=scraped)

    if extracted != "No upcoming tours":
        if not read(extracted=extracted):
            store(extracted=extracted)
            send_email(message=extracted)

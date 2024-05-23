from typing import Any
from datetime import datetime as dt
import sqlite3
import requests
import selectorlib


URL: str = "http://programmer100.pythonanywhere.com"
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
    value = extractor.extract(source)["temperature"]
    
    return value


def store(extracted: Any) -> None:
    """
    Store data in a .db file
    """
    now = dt.now().strftime("%y-%m-%d-%H-%M-%S")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO temperatures VALUES(?,?);", (now, extracted))
    connection.commit()


if __name__ == "__main__":
    scraped = scrape(url=URL)
    extracted = extract(source=scraped)
    store(extracted=extracted)

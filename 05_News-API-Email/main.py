from modules.send_email import send_email
from datetime import datetime
import os
import requests


# Get API_KEY from an Env Variable
API_KEY = os.getenv("NEWS_API_KEY") # Get your key from https://newsapi.org/register
topic = "formula 1"
today = datetime.now().strftime("%Y-%m-%d")
# URL for the request
url = "https://newsapi.org/v2/everything?" \
    f'q="{topic}"&' \
    f"from={today}" \
    "sortBy=popularity&" \
    f"apiKey={API_KEY}&" \
    "language=en"

# Make request
request = requests.get(url=url)
# Get a dictionary with data
content = request.json()
# Initialize email's body
body = "Subject: Formula 1 Today's News\n"
# Access the article titles, description and URLs
for article in content["articles"][0:10]: # First 10 News
    # In case the article doesn't have title
    if article["title"] is not None:
        # Add each article's title, description and URL
        body += article["title"] + "\n" + article["description"] + "\n" + article["url"] + (2 * "\n")

# Send email
body = body.encode("utf-8")
send_email(message=body)

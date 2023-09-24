from flask import Flask, render_template
import pandas as pd


app = Flask(__name__)
# Read the file
filename = "./db/dictionary.csv"
df = pd.read_csv(filename)
# Get only a few columns
words = df[[
    "word"
]]


@app.route("/")
def home():
    # Render HTML and pass a variable
    return render_template("home.html", words=words.to_html())


@app.route("/api/v1/<word>")
def dictionary(word):
    # Get the definition based on a word
    definition = df.loc[df["word"] == word]["definition"].squeeze()
    # Create dictionary
    result = {
        "word": word,
        "definition": definition
    }

    return result


if __name__ == "__main__":
    app.run(debug=True, port=5000)

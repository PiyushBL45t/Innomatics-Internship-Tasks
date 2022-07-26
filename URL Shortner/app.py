from flask import Flask
from flask import render_template
from flask import request
import pyshorteners


app = Flask(__name__)


@app.route("/", methods = ['GET', 'POST'])
def home():
    if request.method == "POST":
        url = request.form.get("url_name")
        s = pyshorteners.Shortener() # Pyshortener object
        short_url = s.tinyurl.short(url)
        return render_template("home.html", url = short_url)
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug = True)

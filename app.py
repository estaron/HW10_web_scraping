from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars_ejs

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_data")


# create route that renders index.html template
@app.route("/")
def home():
    listings = mongo.db.listings.find_one()
    return render_template("index.html", listings=listings)

@app.route("/scrape")
def scrape():
    listings = mongo.db.listings
    listings_data = scrape_mars_ejs.scrape()
    listings.update({}, listings_data, upsert=True)
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)

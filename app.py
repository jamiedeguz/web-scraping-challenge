from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

#create an instance of Flask App
app = Flask(__name__)

#Use flask_pymongo to set up mongo connections
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")


# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    mars = mongo.db.mars.find_one()

    # Return template and data
    return render_template("index.html", mars=mars)

#scrape
@app.route("/scrape")
def scrape():
    mars = mongo.db.mars
    mars_data = scrape_mars.scrape()
    mars.update({}, mars_data,upsert=True)
    return redirect ("/")

if __name__ == "__main__":
    app.run(debug=True)
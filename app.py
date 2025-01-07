
from flask import Flask, render_template, jsonify
from scripts.scraper import scrape_twitter_trends
from scripts.db_handler import save_to_mongodb

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/run-script")
def run_script():
    
    twitter_username = "your_username"
    twitter_password = "your_password"
    proxymesh_url = "http://username:password@proxymesh_url"

    # Run scraper
    data = scrape_twitter_trends(proxymesh_url, twitter_username, twitter_password)

    # Save to MongoDB
    save_to_mongodb(data)

    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)

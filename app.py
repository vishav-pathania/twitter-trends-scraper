
from flask import Flask, render_template, jsonify
from scripts.scraper import scrape_twitter_trends
from scripts.db_handler import save_to_mongodb
from config_loader import load_config

app = Flask(__name__)
config = load_config()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/run-script")
def run_script():
    
    # Load credentials from config
    twitter_username = config["twitter"]["username"]
    twitter_password = config["twitter"]["password"]
    proxymesh_url = config["proxymesh"]["url"]

    # Run scraper
    data = scrape_twitter_trends(proxymesh_url, twitter_username, twitter_password)

    # Save to MongoDB
    save_to_mongodb(data, mongo_uri=config["mongodb"]["uri"], db_name=config["mongodb"]["db_name"])

    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)

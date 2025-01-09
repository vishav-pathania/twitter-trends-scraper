## Twitter Trends Scraper

This project is a web application that scrapes trending topics on Twitter, stores the data in MongoDB, and displays it on a web page. The app uses Flask for the backend, Selenium for web scraping, and MongoDB for storing the data.

## Features

- Scrapes Twitter trending topics using Selenium.
- Saves the data to MongoDB.
- Displays the most recent trends with relevant details on a webpage.
- Ability to run the script to scrape fresh data and view it on the page.
- View the details of the most recent data from MongoDB, including the trends, IP address, and JSON extract of the saved record.

## Technologies Used

- **Flask**: Python web framework for the backend.
- **Selenium**: Web scraping tool for automating browser actions to fetch Twitter trends.
- **MongoDB**: NoSQL database for storing and retrieving the scraped data.
- **JavaScript**: For dynamic content rendering on the front-end.

## Requirements
Before running the project, ensure you have the following installed:

-**Python 3.x**
-**MongoDB (locally or using MongoDB Atlas)**
-**Python dependencies (listed in requirements.txt)**

## Installation

- **1. Clone the repository:**
```bash
git clone https://github.com/vishav-pathania/twitter-trends-scraper.git
cd twitter-trends-scraper
```

- **2. Set up a virtual environment:**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

- **3. Install the required Python dependencies:**
```bash
pip install -r requirements.txt
```

- **4. Set up MongoDB:**

- You can either set up a local MongoDB instance or use MongoDB Atlas for cloud storage.
- Configure your MongoDB URI and database name in config.json.

- **5. Ensure that your config.json contains the necessary credentials for Twitter and the proxy:**
```bash
    {
    "mongodb": {
      "uri": "mongodb+srv://<db_username>:<db_password>@<database_name>.pycwj.mongodb.net/?retryWrites=true&w=majority&appName=<project_name>",
      "db_name": "twitter_trends"
    },
    "twitter": {
      "useremail": "user_email",
      "username": "user_name",
      "password": "user_password"
    },
    "proxymesh": {
      "url": "http://username:userpassword@us.proxymesh.com:port"
    }
  }
```

## Usage

- **1. Run the Flask application:**
```bash
python app.py
```
- **2. Open your browser and visit http://127.0.0.1:5000/ to see the application in action.**

- **3. On the webpage, you can click the "Click here to run the script" button to scrape the latest trends from Twitter. The trends will be displayed on the page along with the timestamp, IP address, and a JSON extract of the data saved to MongoDB.**

- **4. You can click the "Click here to run the query again" button to re-run the script and fetch the latest trends.**
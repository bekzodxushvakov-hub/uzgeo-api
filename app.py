from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/news")
def get_news():
    url = "https://www.uzgeo.uz/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    news_list = []

    articles = soup.find_all("a")

    for a in articles[:20]:
        title = a.get_text(strip=True)
        link = a.get("href")

        if title and link and len(title) > 20:
            news_list.append({
                "title": title,
                "link": link
            })

    return jsonify(news_list)

if __name__ == "__main__":
    app.run(debug=True)
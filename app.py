from flask import Flask, render_template, request
import requests
from config import NEWS_API_KEY

# Create a Flask app
app = Flask(__name__)

# Homepage - Route
@app.route('/')
def index():
    query = request.args.get('query', 'latest')
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    data = response.json()
    articles = data.get('articles', [])
    filtered_articles = [article for article in articles if "Yahoo" not in article["source"]["name"] and 'removed' not in article["title"].lower()]
    return render_template('index.html', articles=filtered_articles, query=query)

if __name__ == '__main__':
    app.run(debug=True)
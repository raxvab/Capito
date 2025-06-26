from flask import Flask, render_template, request, jsonify
import requests
from bs4 import BeautifulSoup
import os

app = Flask(__name__)

def extract_instagram_caption(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        meta_tag = soup.find('meta', property='og:description')
        if meta_tag:
            return meta_tag['content']
        return "Caption not found"
    except Exception as e:
        return f"An error occurred: {e}"

def extract_youtube_description(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        description_tag = soup.find('meta', attrs={'name': 'description'})
        if description_tag:
            return description_tag['content']
        return "Description not found"
    except Exception as e:
        return f"An error occurred: {e}"

def is_valid_url(url):
    return url.startswith("http://") or url.startswith("https://")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/extract', methods=['POST'])
def extract():
    data = request.get_json()
    url = data.get('url', '').strip()
    if not url or not is_valid_url(url):
        return jsonify({'result': "Please enter the URL or your URL is wrong"})
    if "instagram.com" in url:
        result = extract_instagram_caption(url)
        return jsonify({'result': result})
    elif "youtube.com" in url:
        result = extract_youtube_description(url)
        return jsonify({'result': result})
    else:
        return jsonify({'result': "Unsupported URL"})
    
# if __name__ == "__main__":
#     app.run(debug=True)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)


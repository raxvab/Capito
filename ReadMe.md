# Extract Caption

A simple web app to extract captions or descriptions from Instagram Reels and YouTube videos.  
Paste a URL, click **Submit**, and get the caption instantly!

## Features

- 📝 Extracts captions from Instagram Reels and descriptions from YouTube videos
- ⚡ Fast, AJAX-powered UI (no page reloads)
- 🎨 Clean, responsive, and centered design
- 🚫 Alerts for empty or invalid URLs

## Demo

![Screenshot](screenshot.png) <!-- Add a screenshot if you wish -->

## How It Works

1. Paste an Instagram Reel or YouTube video URL.
2. Click **Submit**.
3. The extracted caption/description appears in a scrollable box.

## Tech Stack

- **Frontend:** HTML, CSS, JavaScript (Fetch API)
- **Backend:** Python, Flask, BeautifulSoup, Requests

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/extract-caption.git
cd extract-caption
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
python main.py
```

Visit [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

## Project Structure

```
Capito/
├── main.py
├── requirements.txt
└── templates/
    └── index.html
```

## Notes

- For production or public hosting, use a Python-friendly platform (Render, Railway, Fly.io, Heroku, etc.).
- Instagram and YouTube may block scraping or change their HTML structure, which can break extraction.

## License

MIT

---

**Made with ❤️ using Flask**
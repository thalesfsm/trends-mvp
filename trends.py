import json
import feedparser
from datetime import datetime

URL = "https://trends.google.com/trending/rss?geo=BR"

feed = feedparser.parse(URL)

trends = []

for entry in feed.entries:
    trends.append({
        "trend": entry.title,
        "volume": str(getattr(entry, "traffic", "em alta")),
        "link": entry.link,
        "data": datetime.now().strftime("%Y-%m-%d %H:%M")
    })

with open("trends.json", "w", encoding="utf-8") as f:
    json.dump(trends, f, ensure_ascii=False, indent=2)

print("OK - trends atualizados via RSS")
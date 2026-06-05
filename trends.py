import json
import requests
from datetime import datetime
from xml.etree import ElementTree as ET

URL = "https://news.google.com/rss?hl=pt-BR&gl=BR&ceid=BR:pt-419"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(URL, headers=headers)

root = ET.fromstring(response.content)

items = root.findall(".//item")[:10]

trends = []

for item in items:
    title = item.find("title").text

    trends.append({
        "trend": title,
        "resumo": "Notícia em destaque no Google News no Brasil hoje.",
        "data": datetime.now().strftime("%Y-%m-%d %H:%M")
    })

with open("trends.json", "w", encoding="utf-8") as f:
    json.dump(trends, f, ensure_ascii=False, indent=2)

print("trends.json gerado com sucesso!")
import json
from pytrends_modern import TrendsRSS

rss = TrendsRSS()

trends = rss.get_trends(geo="BR")

resultado = []

for trend in trends[:20]:
    resultado.append({
        "trend": trend["title"],
        "volume": f'{trend["traffic"]}+ buscas'
    })

with open("trends.json", "w", encoding="utf-8") as f:
    json.dump(resultado, f, ensure_ascii=False, indent=2)

print("trends.json gerado com sucesso!")
import json
from datetime import datetime
from pytrends.request import TrendReq

# Conecta no Google Trends
pytrends = TrendReq(hl='pt-BR', tz=360)

# Pega trending searches do Brasil
df = pytrends.trending_searches(pn='brazil')

trends_list = []

for item in df[0].tolist():
    trends_list.append({
        "trend": item,
        "volume": "em alta"  # Google Trends não fornece volume exato aqui
    })

# Salva arquivo JSON
with open("trends.json", "w", encoding="utf-8") as f:
    json.dump(trends_list, f, ensure_ascii=False, indent=2)

print("Trends atualizados com sucesso!")
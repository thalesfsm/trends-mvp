from pytrends_modern import TrendsRSS

rss = TrendsRSS()

trends = rss.get_trends(geo='BR')

for trend in trends:
    print(trend)
import requests
import json

query=input("Enter the topic\n")
r=requests.get(url=f"https://newsapi.org/v2/everything?q={query}&from=2025-10-04&sortBy=publishedAt&apiKey=f3d35d5d28864cd6bcce5b53c090c299")





news=json.loads(r.text)

for i in news.get("articles", []):
        print(i.get('source', {}).get('name'))
        print(i.get("author"))
        print(i.get("title"))
        print("-------------------------------")



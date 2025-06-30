#it is use for provide the news 
#    2364a2b2c5c04001a73f51dfa764083a
import requests
import json

query = input("Enter the which type of news you want ")

url = f"https://newsapi.org/v2/everything?q={query}&from=2025-05-27&sortBy=publishedAt&apiKey=2364a2b2c5c04001a73f51dfa764083a"

r = requests.get(url)
news = json.loads(r.text)

for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("-----------------------------------------------------")

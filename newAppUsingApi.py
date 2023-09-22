import requests
import json

query = input("Which type of news do you want to see: ")
url = f"https://newsapi.org/v2/everything?q={query}&from=2023-08-22&sortBy=publishedAt&apiKey=d50e2c35402243fd93c5cc522cf6179d"
res = requests.get(url)
data = json.loads(res.text)
for i,val in enumerate(data["articles"]):
    print("Title: ",val["title"])
    print("Description: ",val["description"])
    print("=================================================================================================================")
    if i == 5:
        break
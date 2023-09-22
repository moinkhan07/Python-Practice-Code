import requests
import bs4
# resposes = requests.get("https://www.codewithharry.com/")
# print(resposes.text)

# url = "https://jsonplaceholder.typicode.com/posts"
# headers =  {
#     'Content-type': 'application/json; charset=UTF-8',
#   }
# data = {
#     "name": 'Moin Khan',
#     "age": 19,
#     "gender": "Male"
# }
# resposes = requests.post(url,headers=headers,json=data)
# print(resposes.text)


# for web scrapping we use beautifulsoup module "bs4"
url = "https://www.codewithharry.com"
res = requests.get(url)
soup = bs4.BeautifulSoup(res.text,'html.parser')
# print(soup.prettify())
for heading in soup.find_all("h2"):
    print(heading.text)
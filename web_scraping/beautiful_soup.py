import requests
from bs4 import BeautifulSoup

response = requests.get('https://pythonhow.com/example.html')
content = response.content

soup = BeautifulSoup(content, "html.parser")

all = soup.find_all('div', {'class' : 'cities'})

for item in all:
    print("City: " + item.find('h2').text)
    print("Text: " + item.find('p').text)
    print("\n")
import requests
from bs4 import BeautifulSoup

url = 'https://www.youtube.com/watch?v=Mfnwc1dc0MY'

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.find_all(".style-scope")
    print(title)
else:
    print(response.status_code)

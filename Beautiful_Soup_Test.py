import requests
from bs4 import BeautifulSoup

def beautiful_soup_web_scraping(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return str(soup)

url = "https://medium.com/kx-systems/rag-llamaparse-advanced-pdf-parsing-for-retrieval-c393ab29891b"
bs4data=beautiful_soup_web_scraping(url)
print(bs4data)

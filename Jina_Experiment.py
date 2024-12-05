## It will generates md format output so suitable for llm use cases
import requests

def jina_readerapi_web_scraping(url):
    response = requests.get("https://r.jina.ai/" + url)
    return response.text

url = "https://en.wikipedia.org/wiki/Transformers_(film_series)"

data = jina_readerapi_web_scraping(url)

with open("data.md", "w", encoding="utf-8") as file:
    file.write(data)


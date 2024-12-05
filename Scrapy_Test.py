import scrapy

class ExampleSpider(scrapy.Spider):
    name = "example"
    start_urls = ["https://example.com"]

    def parse(self, response):
        title = response.xpath('//title/text()').get()
        print("Page Title:", title)

        links = response.xpath('//a/@href').getall()
        print("Links:", links)

## Usage
"""
pip install scrapy
scrapy runspider Scrapy_Test.py
"""

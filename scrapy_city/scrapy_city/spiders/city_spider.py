import scrapy

class CitySpider(scrapy.Spider):
    name = "city"
    allowed_domains = [
        "city.org",
        "govtech.com"
    ] 
    start_urls = [
        "http://www.city.org/",
        "http://www.govtech.com/"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
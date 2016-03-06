import scrapy

class CitySpider(scrapy.Spider):
    name = "city"
    allowed_domains = [
        "nextcity.org",
        "govtech.com"
    ] 
    start_urls = [
        "http://www.nextcity.org/",
        "http://www.govtech.com/"
    ]

    def parse(self, response):
        for href in response.css("a::attr('href')"):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse)
import scrapy
from scrapy_city.items import ScrapyCityItem

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
        # send the present page down the item pipeline
        item = ScrapyCityItem()
        item['url'] = response.url
        item['html'] = response.body
        yield item
        # traverse the links to get the next items
        for href in response.css("a::attr('href')"):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse)
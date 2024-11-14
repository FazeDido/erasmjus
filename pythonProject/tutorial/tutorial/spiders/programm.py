import scrapy


class ProgrammSpider(scrapy.Spider):
    name = "programm"
    allowed_domains = ["daswerk.org"]
    start_urls = ["https://daswerk.org"]

    def parse(self, response):
        pass

import scrapy
from obedinenie import send_to_telegram

class ProgrammSpider(scrapy.Spider):
    name = "programm"
    start_urls = ["https://www.daswerk.org/programm/"]

    def parse(self, response):
        for event in response.css("div.event-item"):
            event_data = {
                "title": event.css("h2.event-title::text").get(),
                "date": event.css("span.event-date::text").get(),
                "description": event.css("p.event-description::text").get(),
            }
            send_to_telegram(event_data)

        next_page = response.css("li.next a::attr(href)").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

import scrapy
from InformationExtractor import InformationExtractor

MEDIA = "www.paginasiete.bo"
extractor = InformationExtractor()


class PaginaSieteSpider(scrapy.Spider):
    name = "paginasiete"
    start_urls = [elem["enlace"] for elem in extractor.get_media_info_from_api(MEDIA)]

    def parse(self, response):
        yield {
            "title": response.xpath("//title/text()").get(),
            "url": response.url,
            "date": response.xpath("//div[@class='date']").extract(),
            "text": response.css("p::text").getall(),
        }

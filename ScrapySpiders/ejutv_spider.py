import scrapy
from InformationExtractor import InformationExtractor

MEDIA = "eju.tv"
extractor = InformationExtractor()


class PaginaSieteSpider(scrapy.Spider):
    name = "paginasiete"
    start_urls = [elem["enlace"] for elem in extractor.get_media_info_from_api(MEDIA)]

    def parse(self, response):
        # title = response.xpath('//title').extract()
        yield {
            "title": response.xpath("//title/text()").get(),
            "text": " ".join(response.xpath("//body//text()").re(r"(\w+)")),
            "another_way": response.css("p::text").getall(),
        }

import scrapy
from InformationExtractor import InformationExtractor

MEDIA = "www.ahoraelpueblo.bo"
extractor = InformationExtractor()


class PaginaSieteSpider(scrapy.Spider):
    name = "paginasiete"
    start_urls = [elem["enlace"] for elem in extractor.get_media_info_from_api(MEDIA)]

    def parse(self, response):
        # title = response.xpath('//title').extract()
        yield {
            "title": response.xpath("//h1/text()").getall(),
            "url": response.url,
            "date": response.xpath("//time/text()").getall(),
            "text": [
                section.css("p::text").getall()
                for section in response.xpath(
                    "//div[@class='td-post-content tagdiv-type']"
                )
            ],
        }

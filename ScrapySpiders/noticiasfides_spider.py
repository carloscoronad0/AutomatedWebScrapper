import scrapy
from InformationExtractor import InformationExtractor

MEDIA = "www.noticiasfides.com"
extractor = InformationExtractor()

# print(JsonExt.filtered_by_empty_info)


class PaginaSieteSpider(scrapy.Spider):
    name = "noticiasfides"
    start_urls = [elem["enlace"] for elem in extractor.get_media_info_from_api(MEDIA)]

    def parse(self, response):
        yield {
            "title": response.xpath("//title/text()").get(),
            "url": response.url,
            "text": [
                " ".join(
                    line.strip()
                    for line in p.xpath(".//text()").extract()
                    if line.strip()
                )
                for p in response.xpath("//p")
            ],
        }

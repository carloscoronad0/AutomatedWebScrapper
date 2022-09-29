import scrapy
from InformationExtractor import InformationExtractor

MEDIA = "www.lostiempos.com"
extractor = InformationExtractor()

class PaginaSieteSpider(scrapy.Spider):
    name = 'paginasiete'
    start_urls = [elem["enlace"] for elem in extractor.get_media_info_from_api(MEDIA)]

    def parse(self, response):
        #title = response.xpath('//title').extract()
        yield {
            "title": response.xpath('//title/text()').get(),
            "url": response.url,
            "author": response.xpath("//div[@class='autor']").extract(),
            "text": [
                section.css('p::text').getall()
                for section in response.css('div.body')
            ]
        }

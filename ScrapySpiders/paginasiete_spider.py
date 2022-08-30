import scrapy
from JsonInformationExtractor import JsonExtractor

MEDIA = "www.paginasiete.bo"
JsonExt = JsonExtractor(MEDIA)

class PaginaSieteSpider(scrapy.Spider):
    name = 'paginasiete'
    start_urls = [elem["enlace"] for elem in JsonExt.filtered_by_empty_info]

    def parse(self, response):
        yield {
            "title": response.xpath('//title/text()').get(),
            "url": response.url,
            "date": response.xpath("//div[@class='date']").extract(),
            "text": response.css('p::text').getall()
        }

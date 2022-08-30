import scrapy
from JsonInformationExtractor import JsonExtractor

MEDIA = "www.ahoraelpueblo.bo"
JsonExt = JsonExtractor(MEDIA)

class PaginaSieteSpider(scrapy.Spider):
    name = 'paginasiete'
    start_urls = [elem["enlace"] for elem in JsonExt.filtered_by_empty_info]

    def parse(self, response):
        #title = response.xpath('//title').extract()
        yield {
            "title": response.xpath('//h1/text()').getall(),
            "url": response.url,
            "date": response.xpath('//time/text()').getall(),
            "text": [
                section.css('p::text').getall()
                for section in response.xpath("//div[@class='td-post-content tagdiv-type']")
                ]
        }

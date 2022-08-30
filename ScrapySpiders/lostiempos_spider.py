import scrapy
from JsonInformationExtractor import JsonExtractor

MEDIA = "www.lostiempos.com"
JsonExt = JsonExtractor(MEDIA)

print(JsonExt.filtered_by_empty_info)

class PaginaSieteSpider(scrapy.Spider):
    name = 'paginasiete'
    start_urls = [elem["enlace"] for elem in JsonExt.filtered_by_empty_info]

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

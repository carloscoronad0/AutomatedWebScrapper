import scrapy
from JsonInformationExtractor import JsonExtractor

MEDIA = "www.paginasiete.bo"
JsonExt = JsonExtractor(MEDIA)

print(JsonExt.filtered_by_empty_info)

class PaginaSieteSpider(scrapy.Spider):
    name = 'paginasiete'
    start_urls = [elem["enlace"] for elem in JsonExt.filtered_by_empty_info]

    def parse(self, response):
        #title = response.xpath('//title').extract()
        yield {
            "title": response.xpath('//title/text()').get(),
            "text": ' '.join(response.xpath('//body//text()').re(r'(\w+)')),
            "another_way": response.css('p::text').getall()
        }

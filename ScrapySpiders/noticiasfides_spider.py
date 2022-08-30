import scrapy
from JsonInformationExtractor import JsonExtractor

MEDIA = "www.noticiasfides.com"
JsonExt = JsonExtractor(MEDIA)

#print(JsonExt.filtered_by_empty_info)

class PaginaSieteSpider(scrapy.Spider):
    name = 'noticiasfides'
    start_urls = [elem["enlace"] for elem in JsonExt.filtered_by_empty_info]

    def parse(self, response):
        yield {
            "title": response.xpath('//title/text()').get(),
            "url": response.url,
            "text": [
                ' '.join(
                    line.strip() 
                    for line in p.xpath('.//text()').extract() 
                    if line.strip()
                ) 
                for p in response.xpath('//p')
            ]
        }

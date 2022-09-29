import scrapy
from JsonInformationExtractor import JsonExtractor

MEDIA = None
JsonExt = JsonExtractor(MEDIA)

class PaginaSieteSpider(scrapy.Spider):
    name = 'eldeber'
    start_urls = [elem["enlace"] for elem in JsonExt.get_json_data_from_file("../scrapear.json")]

    def parse(self, response):
        #title = response.xpath('//title').extract()
        yield {
            "title": response.xpath("//div[@class='text']//h1//text()").get(),
            "url": response.url,
            "author": response.xpath("//h6//strong/text()").getall(),
            "date": response.css("div.dateNote::text").get(),
            "text": response.xpath("//div[@class='text-editor']//p//text()").getall()
        }

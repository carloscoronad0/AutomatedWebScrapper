from numpy import source
import scrapy
from InformationExtractor import InformationExtractor
from config import PROJECT_PATH

MEDIA = "www.eldeber.com.bo"
extractor = InformationExtractor(source_folder=f"{PROJECT_PATH}/source_info")


class PaginaSieteSpider(scrapy.Spider):
    name = "eldeber"
    start_urls = [
        elem["enlace"]
        for elem in extractor.get_media_info_from_json_file("scrapear.json")
    ]

    def parse(self, response):
        # title = response.xpath('//title').extract()
        yield {
            "title": response.xpath("//div[@class='text']//h1//text()").get(),
            "url": response.url,
            "author": response.xpath("//h6//strong/text()").getall(),
            "date": response.css("div.dateNote::text").get(),
            "text": response.xpath("//div[@class='text-editor']//p//text()").getall(),
        }

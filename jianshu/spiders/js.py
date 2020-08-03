# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from jianshu.items import JianshuItem


class JsSpider(CrawlSpider):
    name = 'js'
    allowed_domains = ['jianshu.com']
    start_urls = ['https://www.jianshu.com/']

    rules = (
        Rule(LinkExtractor(allow=r'.*/p/[0-9a-z]{12}.*'), callback='parse_detail', follow=True),
    )

    def parse_detail(self, response):
        try:
            title = response.xpath("//h1[@class='_1RuRku']/text()").get()
            content = response.xpath("//article[@class='_2rhmJa']").get()
            origin_url = response.url
            avatars = response.xpath("//img[@class='_13D2Eh']/@src").getall()
            image_urls = list(map(lambda avatar: avatar.split('?')[0], avatars))
            pub_time = response.xpath("//div[@class='s-dsoj']/time/text()").get().replace(".", '-')
            author = response.xpath("//span[@class='FxYr8x']/a/text()").get()
            item = JianshuItem(title=title, content=content, origin_url=origin_url, image_urls=image_urls,
                               pub_time=pub_time, author=author)
            yield item
        except Exception as e:
            print(e)
            pass

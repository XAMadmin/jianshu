# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JianshuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    # article_id = scrapy.Field()
    origin_url = scrapy.Field()
    # avatar = scrapy.Field()
    pub_time = scrapy.Field()
    # 存放图片地址
    author = scrapy.Field()
    image_urls = scrapy.Field()
    # 下载成功后返回有关images的一些相关信息
    images = scrapy.Field()

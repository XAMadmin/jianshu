# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import psycopg2
from scrapy.pipelines.images import ImagesPipeline
from . import settings
import os


class JianshuPipeline(object):

    def __init__(self):
        self.conn = None
        self.cur = None

    def open_spider(self, spider):
        # hostname = 'localhost',
        # port = '5432'
        # username = 'postgres'
        # password = 'root'
        # database = 'postgres'
        self.conn = psycopg2.connect(database="postgres", user="postgres", password="root",
                                     host="localhost", port="5432")
        self.cur = self.conn.cursor()

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()

    def process_item(self, item, spider):
        if item:
            self.cur.execute(
                "insert into jianshu(title, content, origin_url, avatar, pub_time, author)"
                " values(%s,%s, %s,%s,%s, %s);", (item["title"],
                                                  item["content"], item["origin_url"],
                                                  item["image_urls"], item["pub_time"], item["author"]))
            self.conn.commit()
        return item


class DownImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        request_objs = super(DownImagePipeline, self).get_media_requests(item, info)
        for request_obj in request_objs:
            request_obj.item = item
        return request_objs

    def file_path(self, request, response=None, info=None):
        path = super(DownImagePipeline, self).file_path(request, response, info)
        author = request.item.get("author")
        image_store = settings.IMAGES_STORE
        author_path = os.path.join(image_store, author)
        if not os.path.exists(author_path):
            os.mkdir(author_path)
        image_name = path.replace("full/", "")
        image_path = os.path.join(author_path, image_name)
        return image_path

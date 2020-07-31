# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from selenium import webdriver
from scrapy.http.response.html import HtmlResponse
import time
import logging
from scrapy.exceptions import NotConfigured
import re


logger = logging.getLogger('Jianshu_Spider')
fh = logging.FileHandler('scrapy.log')
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)


class JianshuSeleniumMiddleware(object):

    def __init__(self):
        self.driver = webdriver.Chrome()

    def process_request(self, request, spider):

        if re.match(r'.*/p/[0-9a-z]{12}.*', request.url) or "https://www.jianshu.com/" == request.url:
            self.driver.get(request.url)
            time.sleep(3)
            source = self.driver.page_source
            response = HtmlResponse(url=self.driver.current_url, body=source, request=request, encoding='utf-8')
            return response
        else:
            pass



class LoggingSpiderMiddleware:
    @classmethod
    def from_crawler(cls, crawler):
        if not crawler.settings.getbool('FILE_LOGGING_ENABLED'):
            raise NotConfigured
        return cls()

    def _msg(self, msg, level=logging.INFO):
        logger._log(level, msg, [])

    # def process_spider_input(self, response, spider):
    #     return None

    def process_spider_output(self, response, result, spider):
        for spider_result in result:
            self._msg('Result: {}'.format(spider_result))
            yield spider_result
        # return result

    def process_spider_exception(self, response, exception, spider):
        self._msg(exception, logging.ERROR)



#!/usr/bin/env python
# encoding: utf-8
"""
bat_dong_san_spider

Copyright (c) 2017 __CGD Inc__. All rights reserved.
"""
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class BatDongSanSpider(CrawlSpider):

    name = 'bat_dong_san'
    allowed_domains = ['batdongsan.com.vn']
    start_urls = [
        'https://batdongsan.com.vn/'
    ]

    rules = (
        Rule(LinkExtractor(allow=(r'.*nha\-dat\-ban\/p\d+$', )), follow=True),
        Rule(LinkExtractor(allow=(r'.*\-pr\d+$', )), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        print "ENTER"
        self.logger.info("PARSER: %s" % response.url)
        return {}

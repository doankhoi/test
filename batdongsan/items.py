# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BatdongsanItem(scrapy.Item):
    address = scrapy.Field()
    area = scrapy.Field()
    price = scrapy.Field()
    description = scrapy.Field()
    room_number = scrapy.Field()
    interior = scrapy.Field()
    contact_mobile = scrapy.Field()
    images = scrapy.Field()


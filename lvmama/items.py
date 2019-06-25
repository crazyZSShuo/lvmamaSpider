# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LvmamaItem(scrapy.Item):
    # define the fields for your item here like:
    # 景点
    name = scrapy.Field()
    # 营业时间
    play_time = scrapy.Field()
    # 地点
    addr = scrapy.Field()
    # 评分
    score = scrapy.Field()
    # 价格
    price = scrapy.Field()
    
    

# -*- coding: utf-8 -*-
import logging

import scrapy

from lvmama.items import LvmamaItem


class LvmaSpider(scrapy.Spider):
	name = 'lvma'
	allowed_domains = ['lvmama.com']
	start_urls = ['http://s.lvmama.com/ticket/K310000P{page}?keyword=上海'.format(page=i) for i in range(1,12)]

	def parse(self, response):
		self.logger.info('Parse page:%s'%response.url)
		all_links = response.xpath("//div[@class='product-section']/h3/a/@href").extract()
		for link in all_links:
			yield scrapy.Request(link,callback=self.parse_info)
	
	
	def parse_info(self,response):
		for jd_info in response.xpath("//div[@class='overview']"):
			item = LvmamaItem()
			item['name'] = jd_info.xpath("//h1/text()").extract()[0] if jd_info.xpath("//h1/text()") else None
			item['play_time'] = jd_info.xpath("//p[@class='canHover']/text()").extract()[0].strip().split('(')[0] if jd_info.xpath("//p[@class='canHover']/text()") else None
			item['addr'] = jd_info.xpath("//p[@class='linetext']/text()").extract()[0] if jd_info.xpath("//p[@class='linetext']/text()") else None
			item['score'] = jd_info.xpath("//div[@class='c_09c']/span/i/text()").extract()[0] if jd_info.xpath("//div[@class='c_09c']/span/i/text()") else None
			item['price'] = jd_info.xpath("//span[@class='price']/dfn/i/text()").extract()[0] if jd_info.xpath("//span[@class='price']/dfn/i/text()") else None
			yield item
		
		

	  

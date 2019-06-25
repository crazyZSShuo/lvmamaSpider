# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo


class LvmamaPipeline(object):
	
	# def process_item(self,item,spider):
	# 	print(item['name'])
	
	# 定义数据表
	collection_name = 'lvmama_info'

	# 初始化连接
	def __init__(self,mongo_uri,mongo_db):
		self.mongo_uri = mongo_uri
		self.mongo_db = mongo_db

	# 从设置中导入数据库地址和数据库
	@classmethod
	def from_crawler(cls,crawler):
		return cls(
			mongo_uri = crawler.settings.get('MONGO_URI'),
			mongo_db = crawler.settings.get('MONGO_DB')
		)

	# 爬虫一旦开启，调用此方法，连接数据库
	def open_spider(self,spider):
		self.client = pymongo.MongoClient(self.mongo_uri)
		self.db = self.client[self.mongo_db]

	# 爬虫关闭，调用此方法，关闭连接
	def close_spider(self,spider):
		self.client.close()


	# 所有的pipeline组件都会调用此方法
	def process_item(self, item, spider):
		self.db[self.collection_name].insert(dict(item))
		return item
		

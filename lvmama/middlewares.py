# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import random

from scrapy import signals





class LvmamaSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class LvmamaDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)



class lvmaSpiderHttpProxyMiddleware(object):

    proxy_list = ['http://121.233.206.158:9999', 'http://163.204.247.157:9999', 'http://182.34.35.176:9999',
			     'http://120.83.103.224:9999', 'http://113.124.86.163:9999', 'http://113.88.209.216:8118',
			     'http://121.233.207.19:9999', 'http://120.83.108.37:9999', 'http://58.58.213.55:8888',
			     'http://112.85.169.218:9999', 'http://112.85.166.159:9999', 'http://112.87.69.122:9999',
			     'http://112.87.68.156:9999', 'http://163.204.245.140:9999', 'http://163.204.247.153:9999',
			     'http://183.63.101.62:53281', 'http://112.87.69.22:9999', 'http://115.53.33.144:9999',
			     'http://112.85.148.189:9999', 'http://120.83.110.178:9999', 'http://120.83.108.111:9999',
			     'http://175.8.109.26:8118', 'http://112.85.168.197:9999', 'http://112.85.164.159:9999',
			     'http://120.83.105.167:9999', 'http://120.83.106.130:9999', 'http://182.138.227.103:8118',
			     'http://112.85.130.234:9999', 'http://120.83.105.209:9999', 'http://120.83.105.84:9999',
			     'http://112.85.171.206:9999', 'http://112.85.130.12:9999', 'http://58.253.153.192:9999',
			     'http://112.87.68.187:9999', 'http://59.32.37.33:61234', 'http://171.80.2.120:9999',
			     'http://120.83.104.109:9999', 'http://120.83.109.202:9999', 'http://182.34.33.103:9999',
			     'http://58.253.159.96:9999', 'http://27.43.186.142:9999', 'http://180.119.68.52:9999',
			     'http://27.43.184.254:9999', 'http://182.34.37.123:9999', 'http://116.208.53.194:9999',
			     'http://171.80.2.89:9999', 'http://60.13.42.91:9999', 'http://183.157.145.212:8118',
			     'http://27.208.19.87:8118', 'http://58.253.155.60:9999', 'http://61.135.155.82:443',
			     'http://222.189.190.171:9999', 'http://112.85.171.61:9999', 'http://1.197.204.168:9999',
			     'http://222.189.190.84:9999', 'http://1.198.72.10:9999', 'http://171.80.1.6:9999',
			     'http://121.233.207.87:9999', 'http://163.204.94.20:9999', 'http://175.10.24.82:3128',
			     'http://171.221.35.93:8118', 'http://115.53.23.137:9999', 'http://1.197.16.77:9999',
			     'http://112.85.130.28:9999', 'http://222.189.190.178:9999', 'http://122.193.247.15:9999',
			     'http://121.233.206.221:9999', 'http://112.85.170.237:9999', 'http://112.87.70.237:9999',
			     'http://218.91.112.209:9999', 'http://58.253.159.246:9999', 'http://112.85.166.207:9999',
			     'http://58.253.155.87:9999', 'http://112.85.170.34:9999', 'http://122.137.16.29:8118',
			     'http://114.230.69.142:9999', 'http://111.226.228.60:8118', 'http://112.85.164.158:9999',
			     'http://180.119.68.223:9999', 'http://112.85.168.21:9999', 'http://163.204.243.252:9999',
			     'http://163.204.247.43:9999', 'http://222.189.191.57:9999', 'http://120.83.121.214:9999',
			     'http://117.91.132.153:9999', 'http://112.87.68.251:9999', 'http://113.121.20.118:9999',
			     'http://171.80.113.39:9999', 'http://222.189.190.211:9999', 'http://112.85.168.184:9999',
			     'http://183.157.173.74:8118', 'http://121.233.207.206:9999', 'http://113.121.20.87:9999',
			     'http://222.189.191.121:9999', 'http://101.200.50.18:8118', 'http://59.32.37.193:8010',
			     'http://1.198.72.46:9999', 'http://1.198.72.45:9999']
    def process_request(self,request,spider):
        ip = random.choice(self.proxy_list)
        print('当前使用的IP：',ip)
        request.meta['proxy'] = ip
    
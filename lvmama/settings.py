# -*- coding: utf-8 -*-

# Scrapy settings for lvmama project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'lvmama'

SPIDER_MODULES = ['lvmama.spiders']
NEWSPIDER_MODULE = 'lvmama.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'lvmama (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# configure maximum concurrent requests performed by scrapy (default: 16)
#concurrent_requests = 32

# configure a delay for requests for the same website (default: 0)
# see https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# see also autothrottle settings and docs

# 下载延迟
#download_delay = 3
# the download delay setting will honor only one of:
#concurrent_requests_per_domain = 16
#concurrent_requests_per_ip = 16

# disable cookies (enabled by default)
cookies_enabled = True

# disable telnet console (enabled by default)
#telnetconsole_enabled = false

# override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
# 	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
# 	'Accept-Language': 'en',
# 	'Access-Control-Allow-Origin': '*',
# 	'Cache-Control': 'no-cache, no-store, must-revalidate',
# 	'Connection': 'keep-alive',
# 	'Content-Encoding': 'gzip',
# 	'Content-Type': 'application/javascript; charset=utf-8',
# 	'Referer':'http://s.lvmama.com',
# 	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
# }

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'lvmama.middlewares.LvmamaSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   # 'lvmama.middlewares.LvmamaDownloaderMiddleware': 543,
	# 'lvmama.middlewares.lvmaSpiderHttpProxyMiddleware':400,
	'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
	'lvmama.middlewares.RandomUserAgentMiddleware':400,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'lvmama.pipelines.LvmamaPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

MONGO_URI = 'mongodb://localhost:27017'
MONGO_DB = 'lvmama'
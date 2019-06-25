from lxml import etree
import requests
import random
import time
import pymongo
import logging



# 抓取所有IP
def get_ips():
	# urls = ['https://www.xicidaili.com/nn/{page}'.format(page=i) for i in range(1,5)]
	# print(urls)
	urls = ['https://www.xicidaili.com/nn/1']
	headers = {
		"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
		"Accept-Encoding": "gzip, deflate, br",
		"Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
		"Cache-Control": "no-cache",
		"Connection": "keep-alive",
		"Host": "www.xicidaili.com",
		"Pragma": "no-cache",
		"Referer": "https://www.xicidaili.com",
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
	}
	ip_dict = {}
	for url in urls:
		print('开始爬取第{}页'.format(url.split('/')[-1]))
		res = requests.get(url,headers=headers)
		print(res.status_code)
		res.encoding = 'utf-8'
		html = etree.HTML(res.text)
		ip_lists = html.xpath("//table[@id='ip_list']")
		for ip in ip_lists:
			ip_dict['ip'] = ip.xpath("//tr/td[2]/text()")
			ip_dict['port'] = ip.xpath("//tr/td[3]/text()")
			print('第{}页共计爬取代理{}个'.format(url.split('/')[-1], len(ip_dict['ip'])))
	return ip_dict



# 验证IP可用性
class Validate_ip(object):
	def __init__(self):
		self.client = pymongo.MongoClient('localhost', 27017)
		self.db = self.client['xiciIP']
		self.ip_info = self.db['ip_info']
		
		self.useful_ips = []
		self.headers = {
			"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
			"Accept-Encoding": "gzip, deflate, br",
			"Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
			"Cache-Control": "no-cache",
			"Connection": "keep-alive",
			"Host": "www.baidu.com",
			"Pragma": "no-cache",
			"Referer": "https://www.baidu.com",
			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
		}
		
	def validate_ips(self,ips):
		
		# ips_list = [(ip,port) for ip,port in zip(ips['ip'],ips['port'])]
		count = 0
		for ip, port in zip(ips['ip'], ips['port']):
			proxies = {
				'http':'http://' + ip + ':'+ port,
			}
			print('开始测试当前IP:{}'.format(proxies['http']))
			# print('开始测试当前IP：',proxies['http'])
			time.sleep(1)
			res = requests.get('https://www.baidu.com',headers=self.headers,proxies=proxies)
			if res.status_code in [200,201]:
				print('验证通过，放心使用!')
				info = {
					'proxy_ip':proxies['http'],
				}
				self.ip_info.insert(dict(info))
				count += 1
			
			# self.useful_ips.append(proxies['http'])
			else:
				continue
		print('数据库插入完毕!!')
		print('共计插入IP：',count)
		self.client.close()
		# return list(set(self.useful_ips))
		
	
	
		
		
if __name__ == '__main__':
	ip_dict = get_ips()
	ip = Validate_ip()
	useful_ips = ip.validate_ips(ip_dict)
	print(useful_ips)
		




import pymongo


client = pymongo.MongoClient('localhost',27017)
db = client['xiciIP']
db_table = db['ip_info']


if __name__ == '__main__':
	print([i['proxy_ip'] for i in db_table.find()])
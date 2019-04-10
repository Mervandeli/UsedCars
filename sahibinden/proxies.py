import random
import requests
class ProxiesMiddleware(object):
    def __init__(self, settings):
        pass

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings)

    def process_request(self, request, spider):
		#url ="http://pubproxy.com/api/proxy?limit=1&format=txt&type=https"
		#data=requests.get(url)
		lines = open('/var/www/html/galeriden.com/scrapy/sahibinden/sahibinden/list.txt').read().splitlines()
		myline =random.choice(lines)
		print(myline)
		request.meta['proxy'] = myline



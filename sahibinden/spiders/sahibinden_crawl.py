


# -*- coding: utf-8 -*-
import scrapy


class SahibindenCrawlSpider(scrapy.Spider):
    name = 'sahibinden-crawl'
    allowed_domains = ['sahibinden.com']
    start_urls = ['https://www.sahibinden.com/otomobil/galeriden?date=1day&pagingSize=50&sorting=date_desc']

    def parse(self, response):
        links=list()
	rows = response.xpath('//*[@class="searchResultsItem"]/td/node()')
     #   rows = response.xpath('//*[@class="searchResultsRowClass"]/tr/node()')
	for row in rows:
		print"***********************************************"
		print row
             	#print row.xpath('//*[@id="searchResultsTable"]/tbody/tr/td[2]/a/@href').extract()

#        next_page_url= response.xpath('//*[@class="pageNaviButtons"]/text()').extract()
#	print next_page_url 
       # yield scrapy.Request("https://sahibinden.com"+next_page_url)

# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.contrib.exporter import CsvItemExporter



class AntigooglewebPipeline(object):


    def spider_opened(self, spider):
    	print(file)
    	print('hh')
    	self.file = open('crawloutput.csv', 'ab')#w+b
    	self.exporter = CsvItemExporter(self.file)
    	self.exporter.start_exporting()

    def process_item(self, item, spider):
    	return item
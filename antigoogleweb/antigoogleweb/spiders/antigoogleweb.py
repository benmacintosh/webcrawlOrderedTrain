import scrapy
from scrapy.spiders import Spider
from antigoogleweb.items import AntigooglewebItem



class antigoogleweb(Spider):
	name = "antigoogleweb"

	allowed_domains=["twitter.com"]
	start_urls = ["https://twitter.com/kanyewest/status/998014241364852738"]
	# allow_domains=["artgallery.nsw.gov.au"]
	# start_urls = ["https://www.artgallery.nsw.gov.au/collection/"]
	# allowed_domains=["tristanhaze.blogspot.com"]
	# start_urls = ["https://tristanhaze.blogspot.com/"]
    


	def parse(self,response):
		for link in response.xpath("//a/@href").extract():
			yield AntigooglewebItem(links=link)

			#self.linkslist.append(link)
			#print(self.linkslist)

		#sel in response.xpath("//p"):
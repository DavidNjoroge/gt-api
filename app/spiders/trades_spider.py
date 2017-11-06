# import scrapy
#
# class TradesSpider(scrapy.Spider):
#     name='trad'
#     # start_urls=['http://www.phoenixtrading.biz/webcat/manufacturers/A/GE-SPEEDTRONIC/DS200_8.shtml']
#
#     def start_requests(self):
#         i=1
#         # i+1
#         urls = [
#         'http://www.phoenixtrading.biz/webcat/manufacturers/A/GE-SPEEDTRONIC/DS200_'+i+'.shtml']
#         for url in urls:
#             yield scrapy.Request(url=url, callback=self.parse)
#     def parse(self,response):
#         yield{'week':
#         for match in response.css('table.list tr[class]'):
#             print('hey hey down here')
#             print(match)
#             yield{
#
#         'part#':match.css('a::attr(href)').extract_first(),
#         'HECI':match.css('td::text').extract()[0],
#         'system':match.css('td::text').extract()[1],
#         'description':match.css('td::text').extract()[2],
#
#
#         }
#         }
#
#         # next_page=response.css('td[width="33%"] font[size="-2"] a::attr(href)').extract_first()
#         # # if next_page is not None:
#         # #     next_page=response.urljoin(next_page)
#         # #     yield scrapy.Request(next_page,callback=self.parse)
#         # for a in response.css('td[width="33%"] font[size="-2"] a'):
#         #     yield response.follow(next_page,callback=self.parse)

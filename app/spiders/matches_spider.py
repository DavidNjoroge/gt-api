# # import scrapy
# weeks=[]
# class MatchesItem(scrapy.Item):
#     home=scrapy.Field()
#     away=scrapy.Field()
#     date=scrapy.Field()
#     # def match(self):
#     #
#     # @classmethod
#     # def week(cls,item):
#     #     week={'week':item}
#     #
#     #     return week
#
#
# class MatchesSpider(scrapy.Spider):
#     name='matches'
#     start_urls=['http://www.stadiumastro.com/sports/epl/results-fixtures/week/10']
#
#     def parse(self,response):
#
#
#         # return weeks
#
#         for day in response.css('div.dayFixtures'):
#             match_day=day.css('h2.sectionTitle::text').extract()
#             for match in day.css('div.matchInfoBox'):
#                 # print(match)
#                 item=MatchesItem()
#
#                 item['home']=match.css('span::text').extract()[0],
#                 item['away']=match.css('span::text').extract()[1]
#                 item['date']=match_day
#                 weeks.append(item)
#
#         yield{'week':weeks}
#         # next_page=response.css('a.nextWeek::attr(href)').extract_first()
#         # if next_page is not None:
#             # next_page=response.urljoin(next_page)
#             # yield scrapy.Request(next_page,callback=self.parse)
#         # for a in response.css('a.nextWeek'):
#         #     yield response.follow(next_page,callback=self.parse)

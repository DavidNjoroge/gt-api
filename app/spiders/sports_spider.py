import scrapy

class SportsSpider(scrapy.Spider):
    name='sports'

    # start_urls=['/home/chutha/Downloads/offline/Week.html']
    start_urls=['http://127.0.0.1:3001/']

    def parse(self,response):


        # for match in response.css('div.matchInfoBox'):
        #     print(match)
        #
        #     yield{
        #
        # 'home':match.css('span::text').extract_first(),
        # 'away':match.css('span::text').extract()[1]
        #
        #
        # }
        for team in response.css('table'):
            yield{
        'team':team.css('tr::text').extract()[1],
        'points':team.css('tr::text').extract()[3]

        }

        # next_page=response.css('a.nextWeek::attr(href)').extract_first()
        # if next_page is not None:
            # next_page=response.urljoin(next_page)
            # yield scrapy.Request(next_page,callback=self.parse)
        # for a in response.css('a.nextWeek'):
        #     yield response.follow(next_page,callback=self.parse)

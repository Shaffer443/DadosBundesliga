import scrapy


class SoccerstatsSpider(scrapy.Spider):
    name = 'JahnRegensburg'
    allowed_domains = ['soccerstats.com']
    start_urls = ['https://www.soccerstats.com/team.asp?league=germany2&stats=9-regensburg']

    def parse(self, response):
           # for dados in response.css('.trow3, .trow2'):
                yield {

                    'Jogos Totais': response.css('.trow3:nth-child(1) font::text').getall()[1:-1],
                    'Gols Totais': response.css('table:nth-child(11) .trow2:nth-child(2) b::text').getall(),
                    'Gols Casa': response.css('table:nth-child(11) .trow2:nth-child(2) td:nth-child(2)::text').getall() ,
                    'Gols Fora': response.css('table:nth-child(11) .trow2:nth-child(2) td:nth-child(3)::text').getall()

                }
        #pass

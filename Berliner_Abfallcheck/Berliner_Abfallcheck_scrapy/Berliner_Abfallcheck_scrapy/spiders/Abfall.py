import scrapy


class AbfallSpider(scrapy.Spider):
    name = 'Abfall'
    allowed_domains = ['berliner-abfallcheck.de']
    start_urls = ['http://berliner-abfallcheck.de/wertstofftonne']
    response=['file:///C:/Users/Louisa/AppData/Local/Temp/tmpbnco6yf3.html']

    def parse(self, response):
        articles=response.css('div.article-content p::text')
        for article in articles:
            print(article)


        pass


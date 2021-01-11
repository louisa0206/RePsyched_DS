import scrapy


class GlascontainerspiderSpider(scrapy.Spider):
    name = 'GlascontainerSpider'
    allowed_domains = ['berlin.de/ba-charlottenburg-wilmersdorf/verwaltung/aemter/umwelt-und-naturschutzamt/umweltschutz/altglascontainer/?q=&q_geo=&q_radius=5000&bemerkungen=#searchresults']
    start_urls = ['https://www.berlin.de/ba-charlottenburg-wilmersdorf/verwaltung/aemter/umwelt-und-naturschutzamt/umweltschutz/altglascontainer/index.php/index/print.html?q=&q_geo=&q_radius=5000&bemerkungen=']
    def parse(self, response):
        Items=response.css('tr.odd.line_1')
        for Item in Items:
            location=Item.css('td.longtext::text').getall()
            print(location)


            ad_Item={
                'location':location
            }

            yield ad_Item



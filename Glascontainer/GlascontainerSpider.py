import scrapy


class GlascontainerspiderSpider(scrapy.Spider):
    name = 'GlascontainerSpider'
    allowed_domains = ['berlin.de/ba-charlottenburg-wilmersdorf/verwaltung/aemter/umwelt-und-naturschutzamt/umweltschutz/altglascontainer']
    start_urls = ['https://www.berlin.de/ba-charlottenburg-wilmersdorf/verwaltung/aemter/umwelt-und-naturschutzamt/umweltschutz/altglascontainer/index.php/index/print.html?q=&q_geo=&q_radius=5000&bemerkungen=']
    def parse(self, response):
        items=response.css('tr')
        for item in items:
            Adress = item.css('tr > td:nth-child(2)::text').get()
            description=item.css('tr > td:nth-child(3)::text').get()
            PLZ=item.css('tr > td:nth-child(4)::text').get()

            ad_item = {
            'Adress':Adress,
            'Description': description,
            'PLZ':PLZ
            }
            yield(ad_item)






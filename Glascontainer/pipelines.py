# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

#useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem

#cleaning dict
class GlascontainerPipeline:
    def process_item(self, item, GlascontainerSpider):
        #deleting unwanted stuff from Adress: just want to keep the street name and delete everything else
        for Entry in item['Adress']:
            if Entry is 'Berlin':
                del(Entry)

        return item







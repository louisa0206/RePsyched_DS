# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

#useful for handling different item types with a single interface
from scrapy.exceptions import DropItem
#importing packages for the coordinates and the translation
import time
from geopy import Nominatim

from google_trans_new import google_translator
translator = google_translator()
# cleaning dict
class GlascontainerPipeline:
    def process_item(self, item, GlascontainerSpider):
        # result is what will be written in csv output
        global address_clean, coordinates, descriptions, Description_clean_ger
        result = {}
        description_uncleaned = item['Description']
        ZIP_Code = item['ZIP-Code']
        # An item that arrives looks for example like this: {'Adress': 'Mecklenburgische Str. 89, 10713 Berlin (',
        # 'Description': 'Aachener Str. Ecke Mecklenburgische Str.', 'PLZ': '10713'}
        # But there could also be items that are not valid, e.g.: {'Adress': None, 'Description': None, 'PLZ': None}
        # we are interested in the address field, so first thing to check is if there is an address available
        if item['Address']:
            # if there is address we want to extract it, by putting it in our result
            address_uncleaned = item['Address']
            # cleaning address
            address_clean= list(map(lambda x: x.replace('Soorstr. 2614050 Berlin', 'Soorstr. 26, 14050').replace('Uhlanstr.', 'Uhlandstr.').replace('(', '').strip(), address_uncleaned))
            address_clean.pop(1)

        #creating the coordinates for the cleaned addresses
        addresses = address_clean
        coordinates = []
        geolocator = Nominatim(user_agent="bl_wt20_repsyched")
        for address in addresses:
            location = geolocator.geocode(address)
            coordinates.append((location.latitude, location.longitude))
                # No heavy uses (an absolute maximum of 1 request per second).
            time.sleep(1)

        if item['Description']:
            #cleaning the Description
            Description_clean_ger = list(map(lambda x: x.replace('ggü.', 'gegenüber').replace('Königin-Elisabeth-Str.', 'Königin-Elisabeth-Straße').replace('Ecke', '/').replace('Hausnummer', 'Nr.').replace('Uhlanstr.', 'Uhlandstr.').replace('vor Nah und gut', '').strip(), description_uncleaned))
            #translate the cleaned Description
            for description in Description_clean_ger:
                Description_eng=translator.translate(description, lang_tgt='en')

            result['Address']=address_clean
            result['Description'] = Description_eng
            result['ZIP-Code'] = ZIP_Code
            result['Latitude, Longitude'] = coordinates
            return result

        else:
            # if there is no Item available we just ignore the item
            raise DropItem('Item is not valid')










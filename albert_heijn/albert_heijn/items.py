# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AlbertHeijnSection(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    link=scrapy.Field()
    name=scrapy.Field()
    pass

class AlbertHeijnProduct(scrapy.Item):
    name=scrapy.Field()
    category=scrapy.Field()
    # price=scrapy.Field()
    # img_link=scrapy.Field()
    # link=scrapy.Field()
    pass




import scrapy
from ..items import AlbertHeijnSection
from ..items import AlbertHeijnProduct

class ProductScraper(scrapy.Spider):
    name="albert"
    start_urls=["https://www.ah.nl/producten"]

    def parse(self, response, **kwargs):
        sections=response.css("a.taxonomy-card_imageLink__13VS1")
        for section in sections:
            AH_Section=AlbertHeijnSection()
            AH_Section["name"]=section.xpath("@title").extract()[0]
            AH_Section["link"]=section.xpath("@href").extract()[0]
            link=self.start_urls[0]+AH_Section["link"]
            yield scrapy.Request(link,self.parse_item_site)


    def parse_item_site(self,response):
        all_products=response.css(".title_lineclamp__1dS7X")
        category=response.css("h1#start-of-content::text").extract()[0]
        for product in all_products:
            AH_Product=AlbertHeijnProduct()
            AH_Product["name"]=product.css("::text").extract()
            AH_Product["category"]=category
            PriceInteger=product.css()
            yield AH_Product



price-amount_integer__1cJgL









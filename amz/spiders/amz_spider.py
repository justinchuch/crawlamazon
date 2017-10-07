# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from scrapy.selector import HtmlXPathSelector
from amz.items import AmzItem
from scrapy.http import Request
from datetime import datetime

class AmzSpider(Spider):
    name = "amz"
    allowed_domains = ["www.amazon.com"]
    start_urls = (
    )
    custom_settings = {
        # exported fields order
        'FEED_EXPORT_FIELDS': ["title", "queryDate", "price", "sale"],
    }

    def parse(self, response):
        # productTitle
        prodTitle = response.xpath('//span[@id="productTitle"]/text()').extract()

        # priceblock_ourprice
        ourPrice = response.xpath('//span[@id="priceblock_ourprice"]/text()').extract()

        # priceblock_saleprice
        salePrice = response.xpath('//span[@id="priceblock_saleprice"]/text()').extract()

        item = AmzItem()

        for titleLine in prodTitle:
            item["title"] = titleLine.strip()

        for priceLine in ourPrice:
            item["price"] = priceLine.strip()

        for saleLine in salePrice:
            item["sale"] = saleLine.strip()

        item["queryDate"] = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        return item

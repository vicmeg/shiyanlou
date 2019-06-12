# -*- coding: utf-8 -*-
import scrapy
from shiyanlou.items import RepositoryItem

class RepositorySpider(scrapy.Spider):
    name = 'repository'
    allowed_domains = ['github.com']

    @property
    def start_urls(self):
        return ('https://github.com/shiyanlou?tab=repositories',)

    def parse(self, response):
        for repository in response.css('li.public'):
            item = RepositoryItem({
                'name': repository.xpath('.//a[@itemprop="name codeRepository"]/text()').re_first('\n\s*(.*)'),
                'update_time': repository.xpath('.//relative-time/@datetime').extract_first()
                })
            yield item

            next_page = response.css('div.BtnGroup a::attr(href)'.extract()[-1]
            yield response.follow(next_page,self.parse)


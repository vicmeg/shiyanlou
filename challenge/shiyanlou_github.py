# _*_ coding: utf-8 _*_

import scrapy

class ShiyanlouGithub(scrapy.Spider):

    name = 'shiyanlou-github'

    @property
    def start_urls(self):
        return ('https://github.com/shiyanlou?tab=repositories',)

    def parse(self,response):
        for repository in response.css('li.public'):
            yield{
                    'name': repository.xpath('.//a[@itemprop="name codeRepository"]/text()').re_first(r'\n\s*(.*)'),
                    'update_time': repository.xpath('.//relative-time/@datetime').extract_first()
                    }
            
            next_page = response.css('div.BtnGroup a::attr(href)').extract()[-1]
            yield response.follow(next_page, callback=self.parse)

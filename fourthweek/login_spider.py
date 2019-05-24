import scrapy, json

class CoursesSpider(scrapy.Spider):
    name = 'courses'

    def start_requests(self):
        return [scrapy.Request(
            url = 'https://www.shiyanlou.com/api/v2/auth/login',
            method = 'POST',
            body = json.dumps({
                'login': '2621276112@qq.com',
                'password': 'Vmic13gt602@rf'
                }),
            headers = {
                'Content-Type':'application/json;charset=UTF-8',
                },
            callback = self.after_parse
            )]

    def after_parse(self,response):
        return scrapy.Request(
                url = 'https://www.shiyanlou.com/users/660408',
                callback = self.parse_after_login
                    )

    def parse_after_login(self,response):
        yield{
                'cs': response.xpath('//ul[@class="user-lab-info-box"]/li[2]'
                        '//li[2]/text()').extract_first().split()[1],
                'sj': response.xpath('//ul[@class="user-lab-info-box"]/li[3]'
                        '//li[2]/text()').extract_first().split()[1]
                    }

import scrapy
from scrapy.linkextractors import LinkExtractor
from newsspiders.items import NewsspidersItem

class IfengSpider(scrapy.Spider):
    name = 'ifeng'
    start_urls =['http://www.ifeng.com/']
    item = NewsspidersItem()
    def parse(self, response):
        urls_list = LinkExtractor(allow=r'news.ifeng.com/a').extract_links(response)
        for url in urls_list:
            href = url.url
            yield scrapy.Request(href,callback=self.download)
    def download(self,response):
        tags = response.xpath("//div[@class='yc_tit' or 'artical']/h1/text()").extract()
        content = response.xpath("//div[@id='yc_con_txt' or 'artical']/p/text()").extract()
        if tags==[]:
            return
        strc = ''
        for x in range(0,len(content)):
            if content[x]:
                strc += content[x]
        self.item['tags'] = tags[0]
        self.item['content'] = strc.strip()
        yield self.item


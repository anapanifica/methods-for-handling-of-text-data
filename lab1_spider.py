import scrapy

class GlossaSpider(scrapy.Spider):
    name = 'GlossaSpider'
    start_urls = ['https://www.glossa-journal.org/articles/']

    def parse(self, response):
        for p in response.xpath('//div[@class="article-section"]/p/text()'):
            yield {'text': p.get()}

        for next_page in response.xpath(
                '//div[@class="col m10 s12"]/a/@href').extract():
            yield response.follow(next_page, self.parse)

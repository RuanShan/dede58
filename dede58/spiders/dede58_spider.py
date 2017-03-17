import scrapy
from scrapy import log

class Dede58Spider(scrapy.Spider):
    name = 'dede58'
    start_urls = ['http://www.dede58.com/a/dedecode/']

    def parse(self, response):
      current_page = response.css('div.page li.thisclass ::text').extract_first()
      next_page =  response.css('div.page li.thisclass+li a[href]')

      for title in response.css('div.project-desc'):
        yield {'title': title.css('p a ::text').extract_first(), 'page': current_page, 'url': response.url}
      print( current_page)
      if next_page:
        print( next_page)
        yield scrapy.Request(response.urljoin(next_page.css('::attr(href)').extract_first()), callback=self.parse)

import scrapy


class TestPlayers(scrapy.Spider):
    name = 'TestPlayers'

    start_urls = ['http://stats.espncricinfo.com/ci/engine/stats/index.html?class=1;filter=advanced;orderby=runs;spanmax1=04+Mar+2019;spanmin1=04+Mar+2018;spanval1=span;team=8;template=results;type=allround']

    def parse(self, response):
        # follow links to author pages
        #for row in response.xpath('//*[@class="engineTable"]//tbody/tr'):
        for href in response.css('a::attr(href)'):
            yield response.follow(href, self.parse_left)
            print (href)
            print ("Udesh Sandeepa Athukorala")
            
    def parse_left(self, response):
        print ("Shiran Umayanga")
        #yield {
        #    'name1': extract_with_css('ciPlayerinformationtext.span::txt'),
        #    'Name' : row.xpath('td[1]//text()').extract_first(),
        # }
        yield {
            'name' : response.css("p.ciPlayerinformationtxt::text").getall(),
            'role' : response.css("p.ciPlayerinformationtxt::text").getall()
        }
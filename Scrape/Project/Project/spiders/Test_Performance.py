import scrapy
 
class TestPerformanceSpider(scrapy.Spider):
    name = "Test_Performance_Table"
 
    def start_requests(self):
        urls = [
            'http://stats.espncricinfo.com/ci/engine/stats/index.html?class=1;filter=advanced;orderby=runs;spanmax1=04+Mar+2019;spanmin1=04+Mar+2018;spanval1=span;team=8;template=results;type=allround',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
 
    def parse(self, response):
        for row in response.xpath('//*[@class="engineTable"]//tbody/tr'):
            #yield row by row data in espn crcinfo performance table, to a json file
            yield {
                'Name' : row.xpath('td[1]//text()').extract_first(),
                'Matches' : row.xpath('td[2]//text()').extract_first(),
                'Runs': row.xpath('td[3]//text()').extract_first(),
                'High Score' : row.xpath('td[4]//text()').extract_first(),
                'Bat Avg' : row.xpath('td[5]//text()').extract_first(),
                '100s' : row.xpath('td[6]//text()').extract_first(),
                'Wickets' : row.xpath('td[7]//text()').extract_first(),
                'BBI' : row.xpath('td[8]//text()').extract_first(),
                '5 wickets' : row.xpath('td[9]//text()').extract_first(),
                'Bowl Avg' : row.xpath('td[10]//text()').extract_first(),
                'Catches' : row.xpath('td[11]//text()').extract_first(),
                'Stumps' : row.xpath('td[12]//text()').extract_first(),
                'Diff' : row.xpath('td[13]//text()').extract_first(),
            }
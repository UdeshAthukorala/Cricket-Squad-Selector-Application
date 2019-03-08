import scrapy
import re
 
class All_vs_IND(scrapy.Spider):
    name = "All_vs_IND_Table"
 
    def start_requests(self):
        #Seperate urls for Test, ODI & T20
        urls = [
            'http://stats.espncricinfo.com/ci/engine/stats/index.html?class=1;opposition=6;spanmin1=05+Mar+2018;spanval1=span;team=8;template=results;type=allround',
            'http://stats.espncricinfo.com/ci/engine/stats/index.html?class=2;opposition=6;spanmin1=05+Mar+2018;spanval1=span;team=8;template=results;type=allround',
            'http://stats.espncricinfo.com/ci/engine/stats/index.html?class=3;opposition=6;spanmin1=05+Mar+2018;spanval1=span;team=8;template=results;type=allround',        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
 
    def parse(self, response):

        MType0 = response.url.split(";")[0]
        MType = MType0.split("?")[1]
        print (MType)
        if (MType == "class=1"):
            MatchType = 'Test'
        elif (MType == "class=2"):
            MatchType = 'ODI'
        elif(MType == "class=3"):
            MatchType = 'T20'

        for row in response.xpath('//*[@class="engineTable"]//tbody/tr'):
            #yield row by row data to a json file

            yield {
                'Type' : MatchType,
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
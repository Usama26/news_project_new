import scrapy

class LinksSpider(scrapy.Spider):
    name = "links"
    start_urls = [
        'https://tribune.com.pk/pakistan',
        'https://dawn.com/pakistan',
    ]

    def parse(self, response):
        final = []
        website_name = response.url.split("https://")[1].split(".com")[0]
        
        if(website_name == 'tribune'):
            targets = response.css('.cat-1.group-0 .title a')
            links = targets.xpath("@href").extract()[:2]
            final.append({
                "website":website_name,
                "links" : links
            })

        elif(website_name == 'www.dawn'):
            targets = response.css('.mb-4 > .story .story__link')
            links = targets.xpath("@href").extract()[:2]
            final.append({
                "website":website_name.split("www.")[1],
                "links" : links
            })
        yield final[0] 

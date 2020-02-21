import scrapy
import pyrebase

class LinksSpider(scrapy.Spider):
    name = "links"
    start_urls = [
        'https://tribune.com.pk/pakistan',
        'https://dawn.com/pakistan',
        'https://techcrunch.com',
        'https://cnet.com/news/'
    ]
    config = {
        "apiKey": "AIzaSyCVFCM6jxRgmfZyuVepfWVFIRd1i3GZctk",
        "authDomain": "newsproject-19880.firebaseapp.com",
        "databaseURL": "https://newsproject-19880.firebaseio.com",
        "storageBucket": "newsproject-19880.appspot.com"
    }

    def parse(self, response):
        final = []
        website_name = response.url.split("https://")[1].split(".com")[0]
        
        print("AAA",self.config)
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

        elif(website_name == 'techcrunch'):
            targets = response.css('.post-block__header .post-block__title a')
            links = targets.xpath("@href").extract()[:2]
            final.append({
                "website":website_name,
                "links" : links
            })

        elif(website_name == 'www.cnet'):
            targets = response.css('.col-4 .assetWrap .assetBody a')
            links = targets.xpath("@href").extract()[:2]

            links = ['https://cnet.com{0}'.format(element) for element in links]
            final.append({
                "website":website_name.split("www.")[1],
                "links" : links
            })

        yield final[0] 

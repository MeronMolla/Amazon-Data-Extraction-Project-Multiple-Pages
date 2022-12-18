
import scrapy
from ..items import AmazonscrapyItem

class AmazonBotSpider(scrapy.Spider):
    
    name = 'amazon-book'
    
    page_number = 1
    
    start_urls = [
        'https://www.amazon.com/s?k=data+science+books&page=1&qid=1669918675&ref=sr_pg_3',
        'https://www.amazon.com/s?k=big+data+book&i=stripbooks&page=1&crid=QQ3TGCX9XDM0&qid=1670013116&sprefix=big+data+boo%2Cstripbooks%2C103&ref=sr_pg_2'
        'https://www.amazon.com/s?k=data+analytics+books&i=stripbooks&page=1&crid=9RD2F40JMIB5&qid=1670014033&sprefix=data+analyti%2Cstripbooks%2C116&ref=sr_pg_2'
        'https://www.amazon.com/s?k=data+science&i=stripbooks&rh=n%3A283155%2Cn%3A5%2Cn%3A549646&s=review-count-rank&dc&page=1&crid=3V8CJ0RV64H3K&qid=1670020455&rnid=283155&sprefix=data%2Cstripbooks%2C94&ref=sr_pg_2'
        ]

    def parse(self, response):
        product=AmazonscrapyItem()
        name=response.css(".a-size-base-plus::text").get()
        price=response.css(".a-price-whole::text").get()
        reviews=response.css(".s-link-style .s-underline-text::text").get()
        author=response.css(".a-color-secondary .s-link-style::text").get()
        url=response.css(".s-image").css("::attr(src)").get()
        product["product_name"]=name
        product["product_price"]=price
        product["product_reviews"]=reviews
        product["author"]=author
        product["product_url"]=url
        
        
        yield product
        
        AmazonBotSpider.page_number +=1
        next_page="https://www.amazon.com/s?k=data+science+books&page="+str(AmazonBotSpider.page_number)+"&qid=1669918675&ref=sr_pg_3"
        next_book_page="https://www.amazon.com/s?k=big+data+book&i=stripbooks&page="+str(AmazonBotSpider.page_number)+"&qid=1670013116&sprefix=big+data+boo%2Cstripbooks%2C103&ref=sr_pg_2"
        next_data_page="https://www.amazon.com/s?k=data+analytics+books&i=stripbooks&page="+str(AmazonBotSpider.page_number)+"&qid=1670014033&sprefix=data+analyti%2Cstripbooks%2C116&ref=sr_pg_2"
        next_bigdata_page= "https://www.amazon.com/s?k=data+science&i=stripbooks&rh=n%3A283155%2Cn%3A5%2Cn%3A549646&s=review-count-rank&dc&page="+str(AmazonBotSpider.page_number)+"&qid=1670020455&rnid=283155&sprefix=data%2Cstripbooks%2C94&ref=sr_pg_2"
        if AmazonBotSpider.page_number<100:
            yield response.follow(next_page, callback=self.parse)
            yield response.follow(next_book_page, callback=self.parse)
            yield response.follow(next_data_page, callback=self.parse)
            yield response.follow(next_bigdata_page, callback=self.parse)
            
            
            
            
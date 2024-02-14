import scrapy

class TestSpider(scrapy.Spider):
    name = "test"
    allowed_domains = ["amazon.de"]
    start_urls = ['https://www.amazon.de/s?k=macbook&__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=16Z7HXR78OCLR&sprefix=macboo%2Caps%2C101&ref=nb_sb_noss_2']

    custom_settings = {
        'FEED_URI': 'data.json',
        'FEED_FORMAT': 'json',
        'FEED_EXPORT_ENCODING': 'utf-8',
    }

    def start_requests(self):
        url = 'https://www.amazon.de/s?k=macbook&__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=16Z7HXR78OCLR&sprefix=macboo%2Caps%2C101&ref=nb_sb_noss_2'
        yield scrapy.Request(url)

    def parse(self, response):
        for price in response.xpath("//span[@class='a-price']"):
            whole = price.xpath(".//span[@class='a-price-whole']/text()").get(default='')
            decimal = price.xpath(".//span[@class='a-price-decimal']/following-sibling::span/text()").get(default='00')
            full_price = f"{whole.replace('.', '').replace(',', '.')},{decimal}"
            yield {'price': full_price}

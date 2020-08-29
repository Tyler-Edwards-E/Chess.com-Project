# -*- coding: utf-8 -*-
import scrapy
import time

# Chess.com Leaderboards Scraper

class ChessSpider3(scrapy.Spider):
    name = 'Match-Spider'
    allowed_domains = ['chess.com']
    rotate_user_agent = True

    username_list = ['hikaru', 'gothamchess', 'lyonbeast'] # , 'gothamchess', 'lyonbeast', '0gZPanda', 'papattack', 'Culum2007', 'catsenlo'

    start_urls=[]
    for i in username_list: # Parses list of usernames above and puts them in the URL
        start_urls+=['https://www.chess.com/games/archive/' + i]
        print(start_urls)

    def parse(self, response):

            HTML = "[Chess.com]--User-Matches-1.html"
            with open(HTML, 'wb') as h2:
                h2.write(response.body)

            print()
            print("Hello")
            print()

            item = {}

            yield item

# ======================================================================================================================================================

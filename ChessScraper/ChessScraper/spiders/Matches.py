# -*- coding: utf-8 -*-
import scrapy
import time

# Chess.com User Matches Scraper

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

            names = response.xpath('.//a[contains(@class, "v-user-popover")]/text()').getall()
            names = [x.strip() for x in names]

            formats = response.xpath('.//span[contains(@class, "archive-games-game-time")]/text()').getall()
            formats = [x.strip() for x in formats]

            for match in response.xpath('//tr[contains(@class, "v-board-popover")]'):

                print()
                print()
                print(match)
                print("=======================================================================================")
                print(match.xpath('.//span[contains(@class, "archive-games-game-time")]/text()').extract_first().strip()) # Format
                print(match.xpath('.//a[contains(@class, "post-view-meta-username v-user-popover")]/text()').getall()) # Usernames
                print()
                print()

            item = {}

            yield item

# ======================================================================================================================================================

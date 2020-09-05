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
                format = match.xpath('.//span[contains(@class, "archive-games-game-time")]/text()').extract_first().strip()

                titles = match.xpath('.//a[contains(@class, "post-view-meta-title v-tooltip")]/text()').getall()
                titles = [x.strip() for x in titles]

                name = match.xpath('.//a[contains(@class, "post-view-meta-username v-user-popover")]/text()').getall()
                name = [x.strip() for x in name]

                ratings = match.xpath('.//span[contains(@class, "post-view-meta-rating")]/text()').getall()
                ratings = [x.strip().replace("(", "").replace(")", "") for x in ratings]

                country = match.xpath('.//div[contains(@class, "post-view-meta-user  ")]/div/@v-tooltip').getall()
                country = [x.strip().replace("'", "") for x in country]

                accuracy = match.xpath('.//td[contains(@class, "table-text-center")]/div/text()').getall()
                if (accuracy == []):
                    accuracy = ["", ""]

                moves = match.xpath('.//td[contains(@class, "table-text-center")]/span/text()').extract()
                moves = moves[0]
                
                date_played = match.xpath('.//td[contains(@class, "table-text-right archive-games-date-cell")]').extract_first().split()
                date_played = date_played[-4] + ' ' + date_played[-3] + date_played[-2]

                whiteName = name[0]
                whiteTitle = titles[0]
                whiteCountry = country[0]
                whiteRating = ratings[0]
                whiteAccuracy = accuracy[0]

                blackName = name[1]
                blackTitle = titles[1]
                blackCountry = country[1]
                blackRating = ratings[1]
                blackAccuracy = accuracy[1]

                # =========================== PRINT TEST ==========================================
                print()
                print()
                print("==================================================================================================")
                # print(match)
                print(format) # Format
                # print(titles) ############ Need solution to only one player having a title
                # print(name) # Usernames
                # print(ratings)
                # print(country)
                print(moves)
                # print(accuracy)
                print(date_played)
                print("---------------------------------------------------------------------")
                print(whiteTitle + " " + whiteName)
                print(whiteCountry)
                print(whiteRating)
                print(whiteAccuracy)
                print()
                print(blackTitle + " " + blackName)
                print(blackCountry)
                print(blackRating)
                print(blackAccuracy)
                print("==================================================================================================")
                print()
                print()

            item = {}

            yield item

# ======================================================================================================================================================

# -*- coding: utf-8 -*-
import scrapy
import time

# Chess.com Leaderboards Scraper

# Parse leaderboard for profile player_links
# Parse leaderboard pages
# Parse profiles

class ChessSpider2Spider(scrapy.Spider):
    name = 'User-Spider'
    allowed_domains = ['chess.com']
    rotate_user_agent = True

    username_list = ['hikaru', 'gothamchess', 'lyonbeast']

    start_urls=[]
    for i in username_list: # Parses list of usernames above and puts them in the URL
        start_urls+=['https://www.chess.com/member/' + i]


    def parse(self, response): # Parse first page leaderboard

            HTML = "[Chess.com]--User-Profile.html"
            with open(HTML, 'wb') as h2:
                h2.write(response.body)

            username = response.xpath('.//h1[contains(@class, "profile-card-username ")]/text()').extract_first()
            if (username != None):
                username = username.strip()

            fullName = response.xpath('.//div[contains(@class, "profile-card-info")]/div/text()').extract_first()
            if (fullName != None):
                fullName = fullName.strip()

            title = response.xpath('.//a[contains(@class, "profile-card-chesstitle ")]/text()').extract_first()
            if (title != None):
                title = title.strip()

            if (response.xpath('.//span[contains(@class, "flair-component flair-diamond_traditional flair-large user-flair-membericon")]/text()').extract_first() != None):
                diamond = 1 # Diamond member = Yes
            else:
                diamond = 0 # Diamond member = Nos

            flag = response.xpath('.//div[contains(@class, "profile-card-flag")]').extract_first()
            flag = str(flag).split()

            for i in flag:
                if ("country" in i):
                    flag.remove(i)
            # if (flag != None):
            #     flag = flag.strip()

# .profile-card-flag div. you can access it with textContent/innerText.
            Date_Collected = time.strftime("%Y-%m-%d")


############ Print Test

            print()
            print("========================================================================================================")
            print()
            print(username)
            print(fullName)
            print(title)
            print(diamond)
            print(flag)
            print()
            print("========================================================================================================")
            print()

            item = {
            }
            yield item

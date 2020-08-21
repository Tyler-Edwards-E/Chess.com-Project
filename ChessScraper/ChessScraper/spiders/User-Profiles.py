# -*- coding: utf-8 -*-
import scrapy
import time

# Chess.com Leaderboards Scraper

# Parse leaderboards and matches for profile likes and post username list here

class ChessSpider2Spider(scrapy.Spider):
    name = 'User-Spider'
    allowed_domains = ['chess.com']
    rotate_user_agent = True

    username_list = ['hikaru', 'gothamchess', 'lyonbeast']

    start_urls=[]
    for i in username_list: # Parses list of usernames above and puts them in the URL
        start_urls+=['https://www.chess.com/member/' + i]

# username, title, legal name, location, country, diamond member, data joined, profile views, followers, points, games played, puzzles completed, lessons lessons_taken,
#       fide rating, blitz rating, rapid rating, puzzles rating, puzzle rush record, daily rating, daily 960 rating, puzzle rush record, daily rating, daily 960 rating,
#       live 960 rating, koth rating, crazyhouse rating, bughouse rating, 3check rating

# Not every user will have values for every column

    def parse(self, response):

            HTML = "[Chess.com]--User-Profile.html"
            with open(HTML, 'wb') as h2:
                h2.write(response.body)

            username = response.xpath('.//h1[contains(@class, "profile-card-username ")]/text()').extract_first()
            if (username != None):
                username = username.strip()

            fullName = response.xpath('.//div[contains(@class, "profile-card-info")]/div/text()').extract_first()
            if (fullName != None):
                fullName = fullName.strip()

            location = response.xpath('.//div[contains(@class, "profile-card-info")]/div/text()').getall() # Name, City, Country
            location = [x.strip() for x in location]
            location.remove('')
            location.remove('')
            location.remove('')
            # Can't use this list to assign final variables because some users may have only a Country and Name, or Country and City, etc.

            title = response.xpath('.//a[contains(@class, "profile-card-chesstitle ")]/text()').extract_first()
            if (title != None):
                title = title.strip()

            if (response.xpath('.//span[contains(@class, "flair-component flair-diamond_traditional flair-large user-flair-membericon")]/text()').extract_first() != None):
                diamond = 1 # Diamond member = Yes
            else:
                diamond = 0 # Diamond member = Nos

            flag = response.xpath('.//div[contains(@class, "profile-card-flag")]').extract_first() # Country is mandatory for Chess.com profiles
            flag = str(flag).split()
            # Having trouble grabbing the text with the country so getting the entire branch and taking only the country

            flag.remove("country-flags-large")
            flag.remove('class="profile-card-flag">')
            flag.remove('class="country-flags-component')
            flag.remove('profile-card-flag-img"></div>')
            flag.remove('</div>')
            flag.remove('<div') # Not being removed with any method for some reason

            for i in flag:
                if ("country" in str(i)): # There are different numbers for each country so can't remove directly
                    flag.remove(i)

            if (len(flag) == 4): # Just in case a country has 3 strings
                country = str(flag[1] + " " + flag[2] + " " + flag[3])
            elif (len(flag) == 3): # '<div', 'United', 'States'
                country = str(flag[1] + " " + flag[2])
            else: # '<div', 'France'
                country = str(flag[1])

            location.remove(country)
            location.remove(fullName)
            if (location != []):
                city = str(location[0])
            else:
                city = ""

            Date_Collected = time.strftime("%Y-%m-%d")


############ Print Test

            print()
            print("========================================================================================================")
            print()
            print(username)
            print(fullName)
            print(title)
            print(diamond)
            # print(flag)
            print(country)
            # print(location)
            print(city)
            print()
            print("========================================================================================================")
            print()

            item = {
            }
            yield item

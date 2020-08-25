# -*- coding: utf-8 -*-
import scrapy
import time

# Chess.com Leaderboards Scraper

# Parse leaderboards and matches for profile likes and post username list here

class ChessSpider2Spider(scrapy.Spider):
    name = 'User-Spider'
    allowed_domains = ['chess.com']
    rotate_user_agent = True

    username_list = ['hikaru', 'gothamchess', 'lyonbeast'] # , 'gothamchess', 'lyonbeast'

    start_urls=[]
    for i in username_list: # Parses list of usernames above and puts them in the URL
        start_urls+=['https://www.chess.com/member/' + i]

# username, title, legal name, location, country, diamond member, data joined, profile views, followers, points, games played, puzzles completed, lessons lessons_taken,
#       fide rating, blitz rating, rapid rating, puzzles rating, puzzle rush record, daily rating, daily 960 rating, puzzle rush record, daily rating, daily 960 rating,
#       live 960 rating, koth rating, crazyhouse rating, bughouse rating, 3check rating

# Not every user will have values for every column

    def parse(self, response):

            HTML = "[Chess.com]--User-Profile-1.html"
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

            profinfo1 = response.xpath('.//div[contains(@class, "profile-info-item-title")]/text()').getall()
            profinfo2 = response.xpath('.//div[contains(@class, "profile-info-item-value")]/text()').getall()
            profileINFO = dict(zip(profinfo1, profinfo2))
            print(profileINFO)

            joined = ''
            online = ''
            views = ''
            followers = ''
            points = ''


            if ("Joined" in profileINFO):
                joined = profileINFO["Joined"]
            if ("Last Online" in profileINFO):
                online = profileINFO["Last Online"]
            if ("Views" in profileINFO):
                views = profileINFO["Views"]
            if ("Followers" in profileINFO):
                followers = profileINFO["Followers"]
            if ("Points" in profileINFO):
                points = profileINFO["Points"]


            item = {
                    'Username': username,
                    'Legal_Name': fullName,
                    'Title': title,
                    'Diamond_Member': diamond,
                    'Country': country,
                    'City': city,
                    'P.Test': profileINFO,
                    'Date_Joined' : joined,
                    'Last_Online': online,
                    'Profile_Views': views,
                    'Followers': followers,
                    'Points': points,
                        }

            stats_link = "https://www.chess.com/stats/live/blitz/" + username

            yield scrapy.Request(response.urljoin(stats_link), dont_filter=True, meta = {'item' : item }, callback= self.stats_page)

# ======================================================================================================================================================

    def stats_page(self, response): # Game stats page

            HTML = "[Chess.com]--User-Profile-2.html"
            with open(HTML, 'wb') as h2:
                h2.write(response.body)

            item = response.meta.get('item', {})

            gametypes1 = response.xpath('.//li[contains(@class, "section-clickable clickable-rating")]/a/@title').getall()
            gametypes1 = [x.strip() for x in gametypes1]

            gametypes2 = response.xpath('.//li[contains(@class, "section-clickable clickable-rating  disable")]/span/h3/text()').getall()
            gametypes2 = [x.strip() for x in gametypes2]
            gametypes2.remove('')
            gametypes2.remove('')
            gametypes2.remove('')
            gametypes2.remove('')

            gametypes22 = response.xpath('.//li[contains(@class, "section-clickable clickable-rating  disable")]/span/h3/span/text()').getall()
            gametypes22 = [x.strip() for x in gametypes22]

            gametypesTWO = dict(zip(gametypes2, gametypes22))

            # Fill variables with blanks if the user doesn't play that gametype
            blitz = ""
            bullet = ""
            rapid = ""
            PRush = ""
            puzzles = ""
            D960 = ""
            daily = ""
            Live960 = ""
            ThreeCheck = ""
            KotH = ""
            Crazy = ""
            Bughouse = ""

            for i in gametypes1:
                if ('Blitz' in i):
                    blitz = i.split()[1]
                elif('Bullet' in i):
                    bullet = i.split()[1]
                elif('Rapid' in i):
                    rapid = i.split()[1]
                elif('Puzzle Rush' in i):
                    PRush = i.split()[2]
                elif('Puzzles' in i):
                    puzzles = i.split()[1]
                elif('Daily 960' in i):
                    D960 = i.split()[2]
                elif('Daily' in i):
                    daily = i.split()[1]

            if ('Live 960' in gametypesTWO):
                Live960 = gametypesTWO["Live 960"]
            if ('3 Check' in gametypesTWO):
                ThreeCheck = gametypesTWO["3 Check"]
            if ('King of the Hill' in gametypesTWO):
                KotH = gametypesTWO['King of the Hill']
            if ('Crazyhouse' in gametypesTWO):
                Crazy = gametypesTWO['Crazyhouse']
            if ('Bughouse' in gametypesTWO):
                Bughouse = gametypesTWO['Bughouse']

            Date_Collected = time.strftime("%Y-%m-%d")

    ############ Print Test
            print()
            print("========================================================================================================")
            print()
            print(item['Username'])
            print(item['Legal_Name'])
            print(item['Title'])
            print(item['Diamond_Member'])
            print(item['Country'])
            print(item['City'])
            print()
            print(gametypes1)
            # print(gametypes2)
            # print(gametypes22)
            print(gametypesTWO)
            print()
            print("Blitz: " + blitz)
            print("Bullet: " + bullet)
            print("Rapid: " + rapid)
            print("Puzzle Rush: " + PRush)
            print("Puzzles: " + puzzles)
            print("Daily 960: " + D960)
            print("Daily: " + daily)
            print("Live 960: " + Live960)
            print("3 Check: " + ThreeCheck)
            print("King of the Hill: " + KotH)
            print("Crazyhouse: " + Crazy)
            print("Bughouse: " + Bughouse)
            print()
            print(item['P.Test'])
            print(item['Date_Joined'])
            print(item['Last_Online'])
            print(item['Profile_Views'])
            print(item['Followers'])
            print(item['Points'])
            print()
            print("========================================================================================================")
            print()

            item2 = {
            }
            yield item2

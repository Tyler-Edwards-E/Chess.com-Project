# -*- coding: utf-8 -*-
import scrapy
import time

# Chess.com Leaderboards Scraper

# Parse leaderboard for profile player_links
# Parse leaderboard pages
# Parse profiles

class ChessSpider1(scrapy.Spider):
    name = 'Leaderboards-Spider'
    allowed_domains = ['chess.com']
    start_urls = ['https://www.chess.com/ratings', 'https://www.chess.com/ratings?page=2', 'https://www.chess.com/ratings?page=3']
    rotate_user_agent = True

    def parse(self, response): # Parse first page leaderboard
        print("-------------------------------------------------------------------------------------------------------")
        print()

        # HTML for Debugging
        HTML = "[Chess.com]--Leaderboards-1.html"
        with open(HTML, 'wb') as h:
            h.write(response.body)

        player_links = response.xpath('.//a[contains(@class, "username")]/@href').getall() # Get all links to player profiles
        print(player_links)
        print()

        R1 = response.xpath('.//div[contains(@class, "master-players-rating-rank")]/text()').getall()
        # Save each world rating on the leadboard page because retired players' profiles don't show their world rating anymore
        R1[:] = [i.strip() for i in R1] # Strip empty space in strings

        R2 = response.xpath('//div[contains(@class, "master-players-rating-player-rank")]/text()').getall()
        R2[:] = [i.strip() for i in R2]

        # Need to seperate values since they have similar xpaths
        WorldRatings = []
        ClassicalRatings = []
        RapidRatings = []
        BlitzRatings = []

        j = 0
        while (j < len(R1)):
            if (j % 2 == 0):
                WorldRatings.append(R1[j])
            else:
                ClassicalRatings.append(R1[j])
            j = j + 1
        k = 1
        while (k < len(R2)):
            RapidRatings.append(R2[k])
            k = k + 3
        k = 2
        while (k < len(R2)):
            BlitzRatings.append(R2[k])
            k = k + 3

        # print(WorldRatings)
        # print(ClassicalRatings)
        # print(RapidRatings)
        # print(BlitzRatings)

        for URL, WR, CR, RR, BR in zip(player_links, WorldRatings, ClassicalRatings, RapidRatings, BlitzRatings): # Pair links and ratings and proceed with parsing profiles
            U = response.urljoin(URL)
            yield scrapy.Request(U, callback = self.parse_profile, meta = {'World_Rank' : WR, 'Classical_Rating' : CR, 'Rapid_Rating' : RR, 'Blitz_Rating' : BR}, dont_filter = True)

    def parse_profile(self, response): # Parse each player profile and create item

        # HTML for Debugging
        HTML2 = "[Chess.com]--Leaderboards-2.html"
        with open(HTML2, 'wb') as h2:
            h2.write(response.body)

            print("-------------------------------------------------------------------------------------------------------")
            print()
            print(response.request.url)

            values1 = response.xpath('.//div[contains(@class, "master-players-name")]/text()').getall()
            values1[:] = [i.strip() for i in values1]
            if ("" in values1):
                values1.remove("")

            values2 = response.xpath('.//div[contains(@class, "master-players-value")]/text()').getall()
            values2[:] = [i.strip() for i in values2]
            if ("" in values2):
                values2.remove("")

            values_dict = dict(zip(values1, values2))

            if (response.xpath('.//div[contains(@class, "stats-value")]/text()').extract_first() != None):
                ranks1 = response.xpath('.//div[contains(@class, "stats-label")]/text()').getall()
                ranks1[:] = [i.strip() for i in ranks1]
                ranks2 = response.xpath('.//div[contains(@class, "stats-value")]/text()').getall()
                ranks2[:] = [i.strip() for i in ranks2]
                ranks = dict(zip(ranks1, ranks2))
                retired = "Active"
            else:
                ranks = {"NotBlitz" : "",
                        "NotRapid" : "",
                        "NotClassical" : ""}
                retired = values_dict["Retired"]

            player_name = response.xpath('.//span[contains(@class, "master-players-full-name")]/text()').extract_first().strip()
            title = response.xpath('.//span[contains(@class, "master-players-chess-title")]/text()').extract_first()
            if (title != None):
                title = title.strip()

            country = values_dict["Federation"]
            born = values_dict["Born"]

            # brithday_split = born.split(" ")
            # month = birthday_split[0]
            # day = birthday_split[0]
            # year = birthday_split[0]
            # age = 2020 - year

            birthplace = values_dict["Place of birth"]

            if ("World Ranking" in ranks):
                WorldRank = ranks["World Ranking"]
            else:
                WorldRank = response.meta.get('World_Rank',{})

            # Some top players don't play all 3 formats so must check if they're in the dictionary
            if ("Rapid" in ranks):
                Rapid = ranks["Rapid"]
            else:
                Rapid = response.meta.get('Rapid_Rating',{})

            if ("Blitz" in ranks):
                Blitz = ranks["Blitz"]
            else:
                Blitz = response.meta.get('Blitz_Rating',{})

            if ("Classical" in ranks):
                Classical = ranks["Classical"]
            else:
                Classical = response.meta.get('Classical_Rating',{})

            Date_Collected = time.strftime("%Y-%m-%d")
            # Print Test
            print(player_name)
            print(title)
            print()
            print(len(values_dict))
            print(values_dict)
            print(country)
            print(born)
            print(birthplace)
            print()
            print(ranks)
            print(WorldRank)
            print(Rapid)
            print(Blitz)
            print(Classical)
            print()
            print(Date_Collected)
            print()

            print("-------------------------------------------------------------------------------------------------------")

            item = {
            "Player_Name" : player_name,
            "Title" : title,
            "Country" : country,
            "Date_of_Birth" : born,
            "Birthplace" : birthplace,
            "World_Rank" : WorldRank.replace("#", ""),
            "Rapid_Rating" : Rapid,
            "Blitz_Rating" : Blitz,
            "Classical_Rating" : Classical,
            "Retired" : retired.replace("in", ""),
            "Date_Collected" : Date_Collected
            }
            yield item

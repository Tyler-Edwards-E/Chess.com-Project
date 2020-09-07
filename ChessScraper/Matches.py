# -*- coding: utf-8 -*-
import scrapy
import time

# Chess.com User Matches Scraper
# Collects data from all Chess.com matches available in a user's recent archive

class ChessSpider3(scrapy.Spider):
    name = 'Match-Spider'
    allowed_domains = ['chess.com']
    rotate_user_agent = True

# Edit this list to collect data on desired Chess.com users
    username_list = ['GMHikaruOnTwitch',
'GothamChess',
'Zablotsky',
'elisak43',
'rostovmaxim',
'DanielNaroditsky',
'Hikaru',
'Komodo_Dragaon',
'Jospem',
'whodee11',
'LikeWater',
'DanielMieles1985',
'Uih7I9kOKokUOhjUJ',
'DagurR',
'theopera',
'AkibaRubi',
'Carudi',
'GM_dmitrij',
'Onischuk_V',
'Leon-Black',
'Guenplen',
'BilodeauA',
'Babafingo_321',
'Izoria123',
'chessfrendz',
'Flawless_Fighter',
'SGchess01',
'Alexander_Kasparov',
'GreenyKnight2001',
'Dracomaniac',
'gagic233',
'AmazingChess210',
'Annawel',
'LyonBeast',
'Openyagami',
'KuzubovYuriy',
'Twitch_ElhamBlitz05',
'BlackBoarder',
'13MiRacLe',
'Fandorine',
'PSvidler',
'youngKID',
'ChessWarrior7197',
'Aleksey_Sorokin',
'bascheyaro',
'Mikasinski',
'RaunakSadhwani2005',
'Kobalia',
'0gZPanda',
'exoticprincess',
'gena217',
'Mazetovic',
'diokletian',
'kuban1991',
'attack2mateU',
'NodariousBIG',
'Sam_ChessMood',
'OK97',
'wannabe2700',
'Hikaru-bot',
'papattack',
'ChristopherYoo',
'Systemcontrol1783',
'DynamicClaim',
'Aguiar94',
'Cryptal',
'Lucas_Tomiello',
'Geoff25',
'JMatias',
'ArjunGuptaDPS',
'FLASH44444',
'FischersFrisoer',
'oganromchess',
'friesnielsen2302',
'elcandado',
'Sofia_Shkidchenko',
'HristyanIliev06',
'Mythili123',
'agencja-seo',
'WhitmanChess',
'jhonnyuribe',
'sergeikim',
'leftrainbow',
'kesav',
'prackid',
'ZEN-22',
'urutodo',
'chinesecoronavirus',
'RedDeath10',
'nadimifar_adnan',
'Culum2007',
'elviejodearriba',
'rapolas12',
'acrawford28',
'Knightonh1',
'Bole07',
'oleg322',
'Valintinian',
'angelmoises',
'sargnagel',
'NormaJean26',
'yuvalater10',
'Mateuhslc',
'Sulthankan',
'airaang',
'NATANcruz',
'Priv93200',
'svchess00001956',
'Vulvik',
'Aldebaran789',
'RickmasterC',
'BulletMercenary',
'bp2004',
'ivanuraev',
'AnishOnYoutube',
'KindaPinkJake',
'SadisticPanda',
'Blitzstream',
'kuli4ik',
'Firouzja2003',
'rpragchess',
'JonahWillow',
'vnkm',
'RedbaronCanada',
'zerxam',
'BrooklynFreestyle',
'TanitoluwaAps116',
'MercurialTwists',
'GOGIEFF',
'Armen_Barseghyan',
'DenLaz',
'mamey78',
'GadimbayliA',
'kakarot_001',
'Sanan_Sjugirov',
'Adham_Fawzy',
'Gannikus21',
'GMBenjaminBok',
'babadroga92',
'chessasuke',
'Vokhidov11',
'jinxy2009',
'irdorath',
'chipmunknau',
'Alexander_Moskalenko',
'Hrant_ChessMood',
'12teen',
'mishikomchedlishvili',
'SantoBlue',
'Saitago',
'FrankieJay',
'Dzej_Double',
'georgeileana',
'MJB223',
'1571Caravaggio',
'grunbergmihai',
'AlekCaissa',
'NguyenDucViet',
'Fantozzi86',
'Pakarma',
'VaheMendelyan',
'trainingguroms',
'littleplotkin',
'Yang_Qindong',
'RodinMihail',
'Asztrik',
'gkbw60',
'djangoreinhardt',
'Grandstodge',
'goldenbeer',
'Aandrew40',
'2_year',
'Da_Kool_Kid',
'LacoIvan',
'drfumbles001',
'stendecc',
'tejasjyade17',
]

    start_urls=[]
    for i in username_list: # Parses list of usernames above and puts them in the URL
        start_urls+=['https://www.chess.com/games/archive/' + i]
        print(start_urls)

    def parse(self, response):

            HTML = "Matches.html"
            with open(HTML, 'wb') as h2:
                h2.write(response.body)

            names = response.xpath('.//a[contains(@class, "v-user-popover")]/text()').getall()
            names = [x.strip() for x in names]

            formats = response.xpath('.//span[contains(@class, "archive-games-game-time")]/text()').getall()
            formats = [x.strip() for x in formats]

            for match in response.xpath('//tr[contains(@class, "v-board-popover")]'):

                format = match.xpath('.//span[contains(@class, "archive-games-game-time")]/text()').extract_first().strip()

                # Selecting the titles is more complicated because you have to handle matches where one player is Titled and the other is not.
                titles = match.xpath('.//div[contains(@class, "post-view-meta-user  ")]/a/text()').getall()
                titles = [x.strip() for x in titles]
                while ("" in titles):
                    titles.remove("")

                whiteTitle = ""
                blackTitle = ""
                j = 0
                while (j < len(titles)):
                    if (len(titles[j]) == 2):
                        if (j == 0):
                            whiteTitle = titles[j]
                        elif (j != 0):
                            blackTitle = titles[j]
                    j = j + 1

                name = match.xpath('.//a[contains(@class, "post-view-meta-username v-user-popover")]/text()').getall()
                name = [x.strip() for x in name]

                ratings = match.xpath('.//span[contains(@class, "post-view-meta-rating")]/text()').getall()
                ratings = [x.strip().replace("(", "").replace(")", "") for x in ratings]

                country = match.xpath('.//div[contains(@class, "post-view-meta-user  ")]/div/@v-tooltip').getall()
                country = [x.strip().replace("'", "") for x in country]

                accuracy = match.xpath('.//td[contains(@class, "table-text-center")]/div/text()').getall()
                if (accuracy == []):
                    accuracy = ["", ""]

                moves = match.xpath('.//td[contains(@class, "table-text-center")]/span/text()').extract_first()

                result = match.xpath('.//div[contains(@class, "archive-games-result-wrapper-score")]/div/text()').getall()
                if (result == ['1', '0']):
                    result = "WHITE"
                elif (result == ['0', '1']):
                    result = "BLACK"
                elif (result == ['½', '½']):
                    result = "DRAW"

                date_played = match.xpath('.//td[contains(@class, "table-text-right archive-games-date-cell")]').extract_first().split()
                date_played = date_played[-4] + ' ' + date_played[-3] + date_played[-2]

                whiteName = name[0]
                whiteCountry = country[0]
                whiteRating = ratings[0]
                whiteAccuracy = accuracy[0]

                blackName = name[1]
                blackCountry = country[1]
                blackRating = ratings[1]
                blackAccuracy = accuracy[1]

                Date_Collected = time.strftime("%Y/%m/%d")
                Time = time.strftime("%H:%M")

                # ===================================== PRINT TEST ==========================================
                print()
                print()
                print("==================================================================================================")
                # print(match)
                print(format)
                # print(titles)
                # print(name)
                # print(ratings)
                # print(country)
                print(moves)
                print(result)
                # print(accuracy)
                print(date_played)
                print(Date_Collected)
                print(Time)
                print("---------------------------------------------------------------------------------------------------")
                print()
                print(whiteTitle + " " + whiteName)
                print(whiteCountry)
                print(whiteRating)
                print(whiteAccuracy)
                print()
                print(blackTitle + " " + blackName)
                print(blackCountry)
                print(blackRating)
                print(blackAccuracy)
                print()
                print("==================================================================================================")
                print()
                print()

                item = {
            'MatchID' : '',
            'Format' : format,
            'Moves_Played' : moves,
            'Result' : result,

            'White_Title' : whiteTitle,
            'White_Player' : whiteName,
            'White_Rating' : whiteRating,
            'White_Accuracy' : whiteAccuracy,
            'White_Country' : whiteCountry,

            'Black_Title' : blackTitle,
            'Black_Player' : blackName,
            'Black_Rating' : blackRating,
            'Black_Accuracy' : blackAccuracy,
            'Black_Country' : blackCountry,

            'Date_Played' : date_played,
            'Date_Collected' : Date_Collected,
            'Time_Collected' : Time
            }

                yield item

# ======================================================================================================================================================

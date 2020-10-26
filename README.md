# Chess.com Project
A personal project demonstrating various data science skills including web scraping, dating analysis, data visualizations, database building, and SQL queries.

## WEB SCRAPING
Everything related to the web scraping and data collection is in the first "ChessScraper" folder. I used the package "scrapy" in Python to web crawl and collect the data. Scrapy auto generates some files and folders when you create a spider, but the manually written scripts are listed below.

*Chess.com-Project/ChessScraper/ChessScraper/spiders/* **Leaderboards.py** : Spider that collects data on each player listed on the top player leaderboards at https://www.chess.com/ratings and creates a dataset. *([Chess.com]-Leaderboards.csv)* 
*Run with **Chess-Leaderboards-Scraper.bat***

*Chess.com-Project/ChessScraper/ChessScraper/spiders/* **User-Profiles.py** : Spider that takes a list of Chess.com users and collects data from their profiles and places them in a dataset. *([Chess.com]-Users.csv)*
*Run with **Chess-User-Scraper.bat***

*Chess.com-Project/ChessScraper/ChessScraper/spiders/* **Matches.py** : Spider that takes a list of Chess.com users collects data on all of their archived matches and places them in a dataset. *([Chess.com]-Matches.csv)*
*Run with **Chess-Match-Scraper.bat***


## DATA ANALYTICS
**(Leaderboards)-Data-Analysis.R** : Data analysis on the data collected from **Leaderboards.py**.

**(Matches)-Data-Analysis.R** : Data analysis on the data collected from **Matches.py**.

**(Users)-Data-Analysis.R** : Data analysis on the data collected from **Users-Profiles**.

## DATA VISUALIZATIONS
**Tableau Visualization** : Folder containing data visuliations made in Tableau of the *"[Chess.com]-Leaderboards.csv"* dataset.

## RELATIONAL DATABASES
**ChessRelationalModel.dmd** : Relational model of a small Chess.com user database made in Oracle Data Modeler.

**ChessRelationalModel.png** : Image of **ChessRelationalModel.dmd**.

**ChessTableGeneration.ddl** : SQL tables generated from **ChessRelationalModel.dmd**.

-----------------------------------------------------------------------

###### WORK IN PROGRESS
- [x] Finish user profiles spider
- [x] Collect list of Chess.com usernames
- [x] Create spider for user matches
- [x] Remake SQL Tables
- [x] Data analysis of user profiles and matches datasets
- [x] Import the datasets into the database
- [ ] Write example SQL queries


# Chess.com Project
A personal project demonstrating various data science skills including web scraping, dating analysis, data visualizations, database building, and SQL queries.

## WEB SCRAPING
Everything related to the web scraping and data collection is in the "ChessScraper" folder. I used the package "scrapy" in Python to collect the data. Scrapy auto generates some files when you create a spider, but the manually written scripts are listed below.

**Leaderboards.py** : Spider that collects data on each player listed on the top player leaderboards at https://www.chess.com/ratings and creates the *"[Chess.com]-Leaderboards.csv"* file

**User-Profiles.py (WIP)** : Spider that takes a list of Chess.com users and collects data from their profiles and places them in a dataset.

## DATA ANALYTICS
**Chess Leaderboards Analysis.R** : Data analysis on the data collected from **Leaderboards.py**.

## DATA VISUALIZATIONS
**Tableau Visualization** : Folder containing data visuliations made in Tableau of the *"[Chess.com]-Leaderboards.csv"* dataset.

## RELATIONAL DATABASES
**ChessRelationalModel.dmd** : Relational model of a small Chess.com user database made in Oracle Data Modeler.

**ChessRelationalModel.png** : Image of **ChessRelationalModel.dmd**.

**ChessTableGeneration.ddl** : SQL tables generated from **ChessRelationalModel.dmd**.


###### WORK IN PROGRESS
- Finish user profiles spider (+ Collect list of Chess.com usernames)
- Create spider for user matches
- Data analysis of user profiles and matches datasets
- Import the datasets into the database
- Write example SQL queries


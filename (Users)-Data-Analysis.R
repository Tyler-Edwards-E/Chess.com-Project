
# Tyler Edwards
# 9 - 12 - 2020
# Chess.com Users Data Analysis

D = read.csv("ChessScraper/[Chess.com]-Users.csv")
str(D) # Checking that all data types are correct

# *** The list of usernames in this dataset were not collected randomly, so there may be bias in the analysis.

hist(D$Blitz)
# First example of bias
# The username list started with higher ranked players, so the following users are also likely to be high ranked

par(mfrow=c(3,4))
hist(D$Blitz); hist(D$Bullet); hist(D$Rapid); hist(D$Puzzle.Rush); hist(D$Puzzles)
hist(D$Daily.960); hist(D$Daily); 
hist(D$Live.960); hist(D$X3.Check); hist(D$King.of.the.Hill)
hist(D$Crazyhouse); hist(D$Bughouse);


CountryCount = as.data.frame(table(D$Country))
# Top 5: United States, Russia, India, Brazil, Ukraine
CityCount = as.data.frame(table(D$City))
# Moscow has the most, but most users don't have a city listed

summary(D$Blitz)
summary(D$Bullet)
summary(D$Rapid)
summary(D$Puzzle.Rush)
summary(D$Puzzle)
summary(D$Live.960)
summary(D$X3.Check)
summary(D$King.of.the.Hill)
summary(D$Crazyhouse)
summary(D$Bughouse)


D.Num = D
Numeric.Cols = unlist(lapply(D.Num, is.numeric))  
D.Num = D.Num[, Numeric.Cols]

Cor = cor(D.Num, use = "pairwise.complete.obs")

# Best Correlations for each format
# Blitz -> Live960
# Bullet -> Live960
# Rapid -> Blitz
# Puzzle Rush -> Bullet
# Puzzles -> Live960
# Daily -> Live960
# Live960 -> Blitz
# 3Check -> Live960
# KOTH -> CrazyHouse
# Crazyhouse -> KOTH
# Bughouse -> Bullet




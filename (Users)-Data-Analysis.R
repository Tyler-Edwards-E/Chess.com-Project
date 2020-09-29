
# Tyler Edwards
# 9 - 12 - 2020
# Chess.com Users Data Analysis

D = read.csv("ChessScraper/[Chess.com]-Users.csv")
str(D) # Checking that all data types are correct
D$Date_Joined = as.Date(D$Date_Joined, "%m/%d/%Y") # Earliest accounts from 2007
D$Date_Collected = as.Date(D$Date_Collected, "%m/%d/%Y")

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

summary(D)

NA.Count = as.data.frame(sapply(D, function(x) sum(is.na(x))))
colnames(NA.Count) = "NAs"
# Blitz is the most played format and Crazyhouse is the least played

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

############## Blitz Modeling 
NA.Count = as.data.frame(colSums(is.na(D)))
# Not using columns with > 2500 NAs in the models

Blitz.LM1 = lm(D$Blitz ~ D$Bullet + D$Rapid + D$Puzzle.Rush + D$Puzzles + 
                 D$Daily + D$Live.960)
summary(Blitz.LM1) # R = 0.9241

# Significant : Bullet, Rapid, Puzzles, Live960
# Insignificant : Puzzle RUsh, Daily

# It's expected that Bullet and Rapid are significant, but interesting that Puzzles are too.

# Removing insignificant factors
Blitz.LM2 = lm(D$Blitz ~ D$Bullet + D$Rapid + D$Puzzles + D$Live.960)
summary(Blitz.LM2) # R = 0.9141




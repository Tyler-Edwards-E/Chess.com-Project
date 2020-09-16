
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
hist(D$Daily.960); #hist(D$Daily); 
hist(D$Live.960); hist(D$X3.Check); hist(D$King.of.the.Hill)
hist(D$Crazyhouse); hist(D$Bughouse);
# Daily is not numeric at the moment



CountryCount = as.data.frame(table(D$Country))



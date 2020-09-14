
# Tyler Edwards
# 9 - 12 - 2020
# Chess.com Users Data Analysis

D = read.csv("ChessScraper/[Chess.com]-Users.csv")
str(D) # Checking that all data types are correct

# *** The list of usernames in this dataset were not collected randomly, so there may be bias in the analysis.

hist(D$Blitz)
# First example of bias
# The username list started with higher ranked players, so the following users are also likely to be high ranked
hist(D$Bullet)

CountryCount = as.data.frame(table(D$Country))



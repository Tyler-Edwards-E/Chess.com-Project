
# Tyler Edwards
# 9 - 12 - 2020
# Chess.com Match Data Analysis

D = read.csv("ChessScraper/[Chess.com]-Matches.csv")
str(D) # Checking that all data types are correct

D$Date_Collected = as.Date(D$Date_Collected, "%m/%d/%Y")

par(mfrow=c(3,2))
hist(D$Moves_Played); hist(D$White_Rating); hist(D$White_Accuracy)
hist(D$Black_Rating); hist(D$Black_Accuracy); 

# Difference between rating (White - Black)
# Analysis showing how much rating influence matches
# Accuracy Difference
# Logit model

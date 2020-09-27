
# Tyler Edwards
# 9 - 12 - 2020
# Chess.com Match Data Analysis

D = read.csv("ChessScraper/[Chess.com]-Matches.csv")
str(D) # Checking that all data types are correct

D$Date_Collected = as.Date(D$Date_Collected, "%m/%d/%Y")
D$White_Country = as.character((D$White_Country))
D$Black_Country = as.character((D$Black_Country))


FormatCount = as.data.frame(table(D$Format))
# 3 min (Blitz) is the highest but there are also some weird formats like "5 days" that I don't know the meaning of

Countrys = as.data.frame(c(D$White_Country, D$Black_Country))
CountryCount = as.data.frame(table(Countrys))
# Top 5 are, United States, Russia, India, France, and Canada

par(mfrow=c(3,2))
hist(D$Moves_Played); hist(D$White_Rating); hist(D$White_Accuracy)
hist(D$Black_Rating); hist(D$Black_Accuracy)

D$Rating.Dif = D$White_Rating - D$Black_Rating
D$Accuracy.Dif = D$White_Accuracy - D$Black_Accuracy

library(tidyverse)
D <- D %>% 
  mutate(Result = recode(Result, 
                    "WHITE" = "0",
                    "DRAW" = ".5",
                    "BLACK" = "1")) %>% 
  mutate(Result = as.numeric(levels(Result))[Result])

D.WL = D[D$Result != .5,] # Dataframe removing all draws

M1 = glm(Result ~ Rating.Dif + Accuracy.Dif, data = D.WL, family = "binomial")
summary(M1)
plot(M1)
# Analysis showing how much rating influence matches
# Logit model


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

Linear.M1 = lm(Result ~ Rating.Dif, data = D)
summary(Linear.M1) # R = 0.1081

Linear.M2 = lm(Result ~ Accuracy.Dif, data = D)
summary(Linear.M2) # R = 0.3388

Linear.M3 = lm(Result ~ Rating.Dif + Accuracy.Dif, data = D)
summary(Linear.M3) # R = 0.3662

# Bothing Rating and Accuracy are significant factors. Accuracy is the better predictors of the two.

D.WL = D[D$Result != .5,] # Dataframe removing all draws so Result is binomial

Logit.M1 = glm(Result ~ Rating.Dif, data = D.WL, family = "binomial")
summary(Logit.M1) # AIC = 9878.7

Logit.M2 = glm(Result ~ Accuracy.Dif, data = D.WL, family = "binomial")
summary(Logit.M2) # AIC = 1853.1

Logit.M3 = glm(Result ~ Rating.Dif + Accuracy.Dif, data = D.WL, family = "binomial")
summary(Logit.M3) # AIC = 1735.5

# Similar conclusion to the linear models, but the Logit model with both factors has the best AIC.


########### Analysis to see if ratings trends with accuracy

RA.W = D[,c("White_Rating", "White_Accuracy")]
RA.B = D[,c("Black_Rating", "Black_Accuracy")]
colnames(RA.W) = c("Rating", "Accuracy")
colnames(RA.B) = c("Rating", "Accuracy")
RA = rbind(RA.W,RA.B)

RA.M1 = lm(RA$Accuracy ~ RA$Rating)
summary(RA.M1)
# Rating is significant, but cannont predict the player's acucracy well

par(mfrow=c(1,1))
plot(RA$Rating, RA$Accuracy)
# This plot might be an example of how the data is skewed with more high rated players.
# There aren't many players in the dataset with a rating below 2000





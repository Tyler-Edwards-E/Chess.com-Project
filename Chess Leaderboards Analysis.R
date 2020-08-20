
# Tyler Edwards
# 7 - 9 - 2020
# Chess.com Leaderboards Data Analysis

library(eeptools)

D = read.csv("C:/Users/Ty/Documents/~~~Chess~~~/ChessScraper/ChessScraper/spiders/[Chess.com]-Leaderboards.csv")
str(D) # Checking that all data types are correct

D$Date_of_Birth = as.Date(D$Date_of_Birth, "%b %d, %Y") # Converting DoB to Date
D$Age = age_calc(D$Date_of_Birth, units = "years") # Adding age column
D$Avg.Rating = (D$Rapid_Rating + D$Blitz_Rating + D$Classical_Rating) / 3 # Combined measure for ratings

Dummies = model.matrix(~D$Country) # Creating dummies for countries
# colnames(Dummies) = gsub("\\$", ".", colnames(Dummies)) # Removing $

D2 = cbind(D, Dummies) # Adding dummies for countries
str(D2)

# ---------------------------------------------------------------------------------

# Summaries of all format ratings
# Rapid
summary(D$Rapid_Rating)
sd(D$Rapid_Rating)
# Blitz
summary(D$Blitz_Rating)
sd(D$Blitz_Rating)
# Classical
summary(D$Classical_Rating)
sd(D$Classical_Rating)

# Boxplots for each format
boxplot(D$Rapid_Rating[D$Rapid_Rating > 2000], # > 2000 drops the 14 year old at around 1500 rating
        D$Blitz_Rating[D$Blitz_Rating > 0], 
        D$Classical_Rating, names = c("Rapid","Blitz", "Classical"))

# ---------------------------------------------------------------------------------

# Correlation between numeric variables

# Rapid + Blitz
cor(D$Rapid_Rating, D$Blitz_Rating, use = "complete.obs") # 0.215
# Rapid + Classical
cor(D$Rapid_Rating, D$Classical_Rating, use = "complete.obs") # 0.633
# Blitz + Classical
cor(D$Blitz_Rating, D$Classical_Rating, use = "complete.obs") # 0.312
# Age + Rapid
cor(D$Age, D$Rapid_Rating, use = "complete.obs") # 0.0001
# Age + Blitz
cor(D$Age, D$Blitz_Rating, use = "complete.obs") # -0.060
# Age + Classical
cor(D$Age, D$Classical_Rating, use = "complete.obs") # -0.181
# Age + Avg.Rating 
cor(D$Age, D$Avg.Rating, use = "complete.obs") # -0.067
# Age + World Rank
cor(D$Age, D$World_Rank, use = "complete.obs") # 0.222
# World Rank + Avg.Rating
cor(D$World_Rank, D$Avg.Rating, use = "complete.obs") # -0.588


# Plots of some of the correlations. (Other plots were already done in Tableau)
plot(D$Rapid_Rating[D$Rapid_Rating > 2000], 
     D$Classical_Rating[D$Rapid_Rating > 2000],
     xlab = "Rapid Rating (>2000)", ylab = "Classical Rating", 
     main = "Rapid vs. Classical Chess Rating")

plot(D$Age, D$World_Rank, main = "Age vs. Chess World Rank", 
     xlab = "Age", ylab = "World Rank")

plot(D$Age, D$Avg.Rating, 
     main = "Age vs. Chess Avg. Rating (Rapid, Blitz, Classical)",
     xlab = "Age", ylab = "Avg. Rating")

plot(D$World_Rank, D$Avg.Rating, 
     main = "Chess World Rank vs. Avg. Rating (Rapid, Blitz, Classical)",
     xlab = "World Rank", ylab = "Avg. Rating")

# ---------------------------------------------------------------------------------

# Linear Modeling

# First model with all numeric columns
WR.M1 = lm(D$World_Rank ~ D$Rapid_Rating + D$Blitz_Rating + D$Classical_Rating
           + D$Age)
summary(WR.M1) # R = 0.8153, Adjusted = 0.8089
# Highly Significant: Intercept, Rapid Rating, Classical Rating
# Significant: Blitz Rating
# Not Significant: Age

# Same model but ratings replaced with average
WR.M2 = lm(D$World_Rank ~ D$Avg.Rating + D$Age)
summary(WR.M2) # R = 0.379, Adjusted = 0.3684
# Highly Significant: Intercept, Avg.Rating
# Significant: Age
# Not Significant:

# Adding country dummy variables to the first model
WR.M3 = lm(D2$World_Rank ~ D2$Rapid_Rating + D2$Blitz_Rating 
           + D2$Classical_Rating + D2$Age + D2$`D$CountryAustria` + D2$`D$CountryAzerbaijan`
           + D2$`D$CountryBelarus` + D2$`D$CountryBelarus` + D2$`D$CountryBulgaria`
           + D2$`D$CountryChina` + D2$`D$CountryCroatia` + D2$`D$CountryCzech Republic`
           + D2$`D$CountryEgypt` + D2$`D$CountryEngland` + D2$`D$CountryFrance`
           + D2$`D$CountryGeorgia` + D2$`D$CountryHungary` + D2$`D$CountryIndia`
           + D2$`D$CountryIran` + D2$`D$CountryIsrael` + D2$`D$CountryNetherlands`
           + D2$`D$CountryNorway` + D2$`D$CountryPeru` + D2$`D$CountryPoland` 
           + D2$`D$CountryRomania` + D2$`D$CountryRussia` +D2$`D$CountrySpain`
           + D2$`D$CountrySweden` + D2$`D$CountryUkraine` + D2$`D$CountryUnited Arab Emirates`
           + D2$`D$CountryUnited States` + D2$`D$CountryUzbekistan` + D2$`D$CountryVietnam`)
summary(WR.M3) # R = 0.8525, Adjusted = 0.799
# Highly Significant: Intercept, Rapid Rating, Classical Rating
# Significant: Blitz Rating
# Not Significant: Age, All country dummies

# Adding country dummy variables to the second model
WR.M4 = lm(D2$World_Rank ~ D2$Avg.Rating + D2$Age 
           + D2$`D$CountryAustria` + D2$`D$CountryAzerbaijan`
           + D2$`D$CountryBelarus` + D2$`D$CountryBelarus` + D2$`D$CountryBulgaria`
           + D2$`D$CountryChina` + D2$`D$CountryCroatia` + D2$`D$CountryCzech Republic`
           + D2$`D$CountryEgypt` + D2$`D$CountryEngland` + D2$`D$CountryFrance`
           + D2$`D$CountryGeorgia` + D2$`D$CountryHungary` + D2$`D$CountryIndia`
           + D2$`D$CountryIran` + D2$`D$CountryIsrael` + D2$`D$CountryNetherlands`
           + D2$`D$CountryNorway` + D2$`D$CountryPeru` + D2$`D$CountryPoland` 
           + D2$`D$CountryRomania` + D2$`D$CountryRussia` +D2$`D$CountrySpain`
           + D2$`D$CountrySweden` + D2$`D$CountryUkraine` + D2$`D$CountryUnited Arab Emirates`
           + D2$`D$CountryUnited States` + D2$`D$CountryUzbekistan` + D2$`D$CountryVietnam`)
summary(WR.M4) # R = 0.5219, Adjusted = 0.3626

# Highly Significant: Intercept, Avg.Rating
# Significant:
# Not Significant: Age, All country dummies

# The model is much better with individual ratings than the Avg.Rating, but the model with 
#       Avg.rating makes Age highly significant where it wasn't significant with the individual ratings.
#       This probably has to do with the fact that younger players aren't highly rated in every category,
#       so their Avg.rating goes down.
# The country dummy variables are all insignificant in predicting world rank regardless of model.
#       This supports the idea that country has no direct involvement in world rank, but a different
#       analysis and larger dataset might be better in showing which countries are better at chess. 


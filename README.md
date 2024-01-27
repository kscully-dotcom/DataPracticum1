# Textile waste predicted by the health of the economy

Kristin Scully – kscully001@regis.edu – (603) 732 -3852

Only 13% of clothing is eventually recycled. (Ellen Macarthur Foundation, 2017) The goal of this research is to identify if there is a relationship between economic collapse, inflation, and the amount of textile waste produced by consumers in the United States. I will perform predictive analysis based on time series data.

I have found 6 datasets.
-	US GDP from 1950 to Q3 2023 from fred.stlouis.gov
-	Monthly Consumer Price Index of clothing and footwear for all US not seasonally adjusted from 2012 to 2023
-	Yearly personal consumption expenditures of clothing, footwear, and related services from 1929 to 2022
-	Yearly inflation of consumer prices for the United States from 1960 to 2022
-	Municipal solid waste categorized by waste type including textiles containing the data from 1960 – 2018. This data includes the weight of materials thrown in landfills, recycled, and combusted.
-	Monthly US Recession data from 1854-2023.

The data will have to transformed to have standardized date ranges and limit municipal solid waste to just data based on textiles. I will use the metrics of GDP, CPI, personal consumption expenditures, inflation, whether the country was in a recession or not, and the municipal solid weight amount of textile waste to determine whether the waste will go up or down in years past 2018 based on the economic health of the country. I will use feature selection methods alongside supervised machine learning algorithms to determine the predictions. I will compare several machine learning algorithms to determine the best algorithm to use and why those algorithms produce greater results.

The dates aren’t a one-to-one match across the features and the consumer price index is not seasonally adjusted. I will have to keep a close eye on trends that surround holidays or times of year when prices or consumer expenditures would increase and adjust accordingly. If there is a certain time of year when prices are higher for all years included in the dataset I will then either take note of the trend for my analysis or adjust for seasonality.


# Textile waste predicted by the health of the economy

Kristin Scully – kscully001@regis.edu

Only 13% of clothing is eventually recycled. (Ellen Macarthur Foundation, 2017) The goal of this research is to identify if there is a relationship between economic collapse, inflation, and the amount of textile waste produced by consumers in the United States. I will perform predictive analysis based on time series data.

I have found 6 datasets.
-	US GDP from 1950 to Q3 2023 from fred.stlouis.gov
-	Monthly Consumer Price Index of clothing and footwear for all US not seasonally adjusted from 2012 to 2023
-	Yearly personal consumption expenditures of clothing, footwear, and related services from 1929 to 2022
-	Yearly inflation of consumer prices for the United States from 1960 to 2022
-	Municipal solid waste categorized by waste type including textiles containing the data from 1960 – 2018. This data includes the weight of materials thrown in landfills, recycled, and combusted.
-	Monthly US Recession data from 1854-2023.

The data is transformed to have standardized date ranges and limit municipal solid waste to just data based on textiles. I used the metrics of GDP, personal consumption expenditures, inflation, whether the country was in a recession or not, and the municipal solid weight amount of textile waste to determine whether the waste will go up or down in years past 2018 based on the economic health of the country. I used intuitive feature selection methods alongside supervised machine learning algorithms to determine the predictions. I compared several machine learning algorithms to determine the best algorithm to use and why those algorithms produce greater results.

# Results
![image](https://github.com/kscully-dotcom/DataPracticum1/assets/78189067/ca958efb-7bf9-44b7-a7b7-1a385102796a)
![image](https://github.com/kscully-dotcom/DataPracticum1/assets/78189067/15d60412-3233-459c-b25a-fd21fe2abd1b)

![image](https://github.com/kscully-dotcom/DataPracticum1/assets/78189067/00a00bd5-1ff1-493d-aa37-724f5803a5b8)
![image](https://github.com/kscully-dotcom/DataPracticum1/assets/78189067/f3cf3d49-93e7-4964-a980-c7d1bc476b26)

![image](https://github.com/kscully-dotcom/DataPracticum1/assets/78189067/09a42925-6152-46db-8331-5faadb9eaee2)
![image](https://github.com/kscully-dotcom/DataPracticum1/assets/78189067/97ffe350-cfab-49b1-a910-48b7c034b81b)

![image](https://github.com/kscully-dotcom/DataPracticum1/assets/78189067/59a79f13-b67d-4338-a108-fdeb950cb54a)
![image](https://github.com/kscully-dotcom/DataPracticum1/assets/78189067/2f83dfe4-c27d-4d50-a34d-43f9b4cf68b7)



- As GDP rises, so does waste generation.
- Non-normalized forward fill had the best regression models according to p-value
- Overall, the results were poor for every model because the economic factors chosen did not explain the waste generation
- The regression model you choose doesn’t matter if the predictor variables don’t explain the target variable
- More effort is needed to find variables that correlate with the target variable

# Next Steps
- Find or develop predictor variables that better explain the waste generation.
- Research waste management processes within the largest textile producers
- Do more sustainable producers produce less waste?
- Can implementation of new technologies reduce the waste generation of textiles?

Things Learned:
- Be prepared to pivot your research during the EDA stage, when you find out the relationship between predictor variables and target variables

Ellen Macarthur Foundation. (n.d.) A new textiles economy: Redesigning fashion’s future. Ellen Macarthur Foundation. https://www.ellenmacarthurfoundation.org/a-new-textiles-economy

Scully, K. (2023) Internet of things – Technology as a waste solution for the textile supply chain. Department of Computer Science, Regis University. pp. 2-14.





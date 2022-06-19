# Phase 2 Project RL 

## Project Overview
In this project, we are focused on creating a multilinear regression model after exploratory data analysis. Throughout our exploratory data anaylsis we found several factors that influence the price, thus these factors were selected and delinated into external versus internal. We used squarefoot living space as our first continuous variable followed by OHE variables such as Grade, Condition, View etc.

### Business Problem
The housing bubble is about to pop and I am working with a real estate company to help identify profitable houses to purchase and easily resell. This project helps to create weights for certain attributes of the house, such as squarefoot living space, waterfront presence etc. The coefficients are the weight of the influence a factor has on price (our target variable). Ideally, we would be able to want an umbrella view of all the coefficients, which then can give us an insight on whether a house is overvalued or undervalued.

Throughout my EDA I have encountered questions (hypotheses) such as: Does having a waterfront, view,sqft_15 improve the average price of a house in the area (in my opinion an external factor)? Or, Does having a basement improve the average price of the house(an internal categorical variable). Or, Does having an extra bathroom improve the price(internal categorical)? Etc. My hypothesis is that the cost of the house is derived more from internal factors than external.I then use my final model and coefficients to see which ones have a positive or negative influence on the target variable(price).

### The Data

In the folder "Data" is the JSON.GEO file for our folium package.
There is also the Kings County Dataset 

#### How is the data?
Throughout my EDA I have encountered questions (hypotheses) such as: Does having a waterfront, view,sqft_15 improve the average price of a house in the area (in my opinion an external factor)? Or, Does having a basement improve the average price of the house(an internal categorical variable). Or, Does having an extra bathroom improve the price(internal categorical)? Etc. My hypothesis is that the cost of the house is derived less from internal factors than external.I then use my final model and coefficients to see which ones have a positive or negative influence on the target variable(price).

### Key Points **Three business recommendations.** 

* External factors display a higher impact on price in the EDA, the model (which has a 71.7% explanation for variance in prices) helps us verify our hypothesis)

* Having a waterfront increases the price most drastically out of all the factors provided

* Condition of the house is usually correlated with a decrease in price, which is an internal factor. When it is positively correlated with price, it usually in a "very good condition" 


#### Links

* [Link to Notebook] https://github.com/RaymondLeong94/dsc-phase-2-project-v2-3/blob/main/data/Phase%202%20Project%20RL%20.ipynb
* [Link to presentation] https://github.com/RaymondLeong94/dsc-phase-2-project-v2-3/blob/main/Impact%20of%20Internal%20and%20External%20Factors%20of%20Houses%20Final.pdf


### Data Manipulation
* EDA and preprocessing
  * Averages were found for each category within the domains of: Grade, Condition, and view via a cascading drop technique.
  * Most outliers were kept in the model unless the final model violated the assumptions of MultiLinear Regression
  * I never touched the price target variable but indirectly dropped some rows by looking at other independent variables (such as bathrooms and rooms).
  * Transformed Basement, waterfront without OHE
  * Transformed view, grade, waterfront with OHE
  * Target variable was log-transformed 
  
* Tables
  * Pivoted the tables to help get counts for zipcodes 
  * NAN values were excluded
      
### Results

![image](https://user-images.githubusercontent.com/98904682/174501563-6e0b5b33-df47-4fa8-828f-363ec842565a.png)
* This heatmap shows us all the continuous variables and their correlations to price 

![image](https://user-images.githubusercontent.com/98904682/174501577-a17e1ad7-4bbe-4976-9e6d-3b76bf110511.png)
* This shows the KDE and quantile distribution of price, our target variable 

![image](https://user-images.githubusercontent.com/98904682/174501611-69c20b6e-cad4-480d-9f00-f47657f1751e.png)
* Folium map of houses sold in Kings County, WA

![image](https://user-images.githubusercontent.com/98904682/174501640-bca6e508-d794-4b5c-a645-791dcd06a43c.png)
* This graph shows prices of houses with varying views

![image](https://user-images.githubusercontent.com/98904682/174501651-23d11b46-ed68-4453-b606-83dc9392425b.png)
* This one shows prices of houses with varying conditions

![image](https://user-images.githubusercontent.com/98904682/174501667-b3160d04-964b-45d1-b7c2-dc69ea649137.png)
* This was engineered to show the trend between the average price of a house listed at a certain grade

### Modelling and Regression Results  
* [Link to model] https://github.com/RaymondLeong94/dsc-phase-2-project-v2-3/blob/main/data/final_model.sav
* Overall, our model explains 71.7% of the total variances observed and predicts the price with a RMSE less than 2.
* All p values that were >.05 were dropped except for the coefficient "Grade_13_Mansion", which is explained in the notebook, alpha value was .05.

![image](https://user-images.githubusercontent.com/98904682/174502084-564e44e3-13d0-47e9-a8cb-a78f4429bff4.png)
* QQ plot to examine Residuals

![image](https://user-images.githubusercontent.com/98904682/174502099-236d870b-4448-4cbc-87a7-8b391d28a77a.png)
* Homoscedasticity results

![image](https://user-images.githubusercontent.com/98904682/174502112-1d4b0a95-21c6-4ad5-b7e8-54d83fa59837.png)
* Distribution of residuals

### Conclusion
* External factors influence the pricing of a house more than internal factors in our model
* Waterfronts, Excellent Views from the house are the biggest influencers on the price of the house.
* Long/lat coordinates (North and West) have a correlation with an increase in house prices as you go towards waterfronts

### Commit History 
* First commit was the final draft of the project

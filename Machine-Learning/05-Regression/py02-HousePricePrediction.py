"""
Example 3: Price of the house is actually dependent on more than 1 factor (`multiple-variables`). 
Let's say 3 factors, Area, Number of Bedrooms and Age. In a real-world scenario, 
this is what we want to be doing right? 
* Our `Target Variable / Dependent Variable` is Prices, because that is the variable that 
we are trying to predict.
* `Features or Independent Variables` are Area, Number of Bedrooms and Age of house.
"""
# Import the homeprices.csv
# Put it into pandas dataframe
# Fit it to the Linear Regression Model
# Plotting the Graph

import numpy as np
import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt
import math

# Import csv
dataset = pd.read_csv("data/homeprices.csv")

# Fill missing values
median_bedrooms = math.floor(dataset.bedrooms.median())
dataset.bedrooms = dataset.bedrooms.fillna(median_bedrooms)

# Fit the linear regression model
model = linear_model.LinearRegression()
x = dataset[['area', 'bedrooms', 'age']]
y = dataset[['price']]
model.fit(x, y)

# Find out the y intercept and co-efficients
m1 = model.coef_[0][0]
m2 = model.coef_[0][1]
m3 = model.coef_[0][2]
c = model.intercept_

print(f"m1 = {m1}, m2 = {m2}, m3 = {m3}, c = y-intercept = {c}")

# Find price of home with 3000 sqr ft area, 3 bedrooms, 40 year old
model.predict([[3000, 3, 40]])
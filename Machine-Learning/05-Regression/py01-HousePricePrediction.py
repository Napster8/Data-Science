"""
Example 1: Area of the houses in Monroe Twp, NJ (USA) and their historical House prices:

    * Areas:  2600, 3000, 3200, 3600, 4000
    * Prices: 550000, 565000, 610000, 680000, 725000

"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model

# Creating Pandas series

# Features = x = areas
# variable that we are trying to predict = y = Prices
x = pd.Series([2600, 3000, 3200, 3600, 4000])
y = pd.Series([550000, 565000, 610000, 680000, 725000])

# Creating Pandas DataFrame
dataset = pd.DataFrame({'Areas': x, 'Prices': y})

# Fitting the Linear Regression model
model = linear_model.LinearRegression()
model.fit(dataset[['Areas']], dataset.Prices)

# Observing the slope and predictions
m = model.coef_
c = model.intercept_
print(f'm = {m[0]} and c = {c}')

# If, Area = 3300, then Price = ?
model.predict([[3300]])
print(
    f'If the area is 3300, then the price of the house would be: {model.predict([[3300]])}')

# If, Area = 5000, then Price = ?
model.predict([[5000]])
print(f'If the area is 5000, then the price = {model.predict([[5000]])}')

# Plots
fig, ax = plt.subplots()
# scatter points
ax.scatter(x, y)
ax.set(title='Area of the houses in Monroe Twp, NJ (USA) and their Prices',
       xlabel='Areas',
       ylabel='Prices')

# Plotting the Fit line: ax.plot(x-axis, y-axis, color = "red")
# plot(x features, y-prediction, color = '')
ax.plot(dataset.Areas, model.predict(dataset[['Areas']]), color="red")

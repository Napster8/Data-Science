"""
Assuming that the linear regression curve suits the given problem present in the hiring.csv contains hiring stats for a firm such as experience of candidate, his written test score and personal interview score. Based on these 3 factors, HR will decide the salary. Given this data, you need to build a machine learning model for HR department that can help them decide salaries for future candidates. Using this predict salaries for following candidates,

    2 yr experience, 9 test score, 6 interview score

    12 yr experience, 10 test score, 10 interview score

Hint: Useword2numbermodule.OfficialDocumentation: https: // pypi.org / project / word2number / 1.1 /

"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
from sklearn import linear_model
import math

 
dataset = pd.read_csv("data/hiring.csv")

# Data-Pre-Processing:

    # Rewrite the column names.
    # Fill NaN values with 0 in experience column.
    # Convert words to numbers in the experience column.
    # Fill NaN values with mean score (rounded off) in test_score column.



# Fill the missing value with median value of the number of bedrooms in the entire dataset
dataset.rename(columns = {'test_score(out of 10)':'test_score',
                          'interview_score(out of 10)':'interview_score',
                          'salary($)': 'salary'}, inplace=True)

# Fill NaN values with 0 in experience column                        
dataset.experience = dataset.experience.fillna(0)

# Convert words to numbers in the experience column
dataset.experience = dataset.experience.apply(w2n.word_to_num)

# Convert to string and replace the words with num
from word2number import w2n
dataset.experience = dataset.experience.apply(str)
dataset.experience = dataset.experience.apply(w2n.word_to_num)
dataset

# Fill NaN values with mean score (rounded off) in test_score column
test_score_mean = math.floor(dataset.test_score.mean())
dataset.test_score = dataset.test_score.fillna(test_score_mean)

# Fit the model
model = linear_model.LinearRegression()
model.fit(dataset[['experience', 'test_score', 'interview_score']], dataset['salary'])

# Make predictions
print(model.predict([[12, 10, 10]]))

print(model.predict([[2,9,6]]))
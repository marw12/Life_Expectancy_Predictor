# -*- coding: utf-8 -*-
"""Life_expectancy.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nh4ewTbt9emnq2oX8i2DtbgRhaqBZukl

## Data Preprocessing
"""

# Importing the libraries
import numpy as np
import pandas as pd
import tensorflow as tf
import pickle
tf.__version__


# Importing the dataset
dataset = pd.read_csv('WHO.csv')
dataset = dataset.round(decimals=2)
X = dataset.iloc[0:1000, [2,4,5,6,8,10,11,12,13,14,15,18,19,20,21]].values
y = dataset.iloc[0:1000, 3].values

print(X)

# Taking care of missing data
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values = np.nan, strategy = 'mean')
imputer.fit(X[:, 1:21])
X[:, 1:21] = imputer.transform(X[:, 1:21])

# Label Encoding 
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
X[:, 0] = le.fit_transform(X[:, 0])
print(X)

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Training the Multiple Linear Regression model on the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)
np.set_printoptions(precision=1)
print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))

#getting equation with coeff.
print(regressor.coef_)
print(regressor.intercept_)

# Saving model to disk
pickle.dump(regressor, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))
print("predict:" , regressor.predict([[0,6,1,9.71,91,66.1,1,92,9.42,92,0.1,0.6,0.6,0.936,20.4]]))
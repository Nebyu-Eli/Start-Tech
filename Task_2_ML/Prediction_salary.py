# -*- coding: utf-8 -*-
"""
Created on Fri May  6 08:30:16 2022

@author: hp
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


dataset = pd.read_excel('Data_file.xlsx')
X = dataset.iloc[2:,1:8].values
y = dataset.iloc[2:,8].values
y = y.tolist()
y = np.array(y)
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[:,2] = labelencoder_X.fit_transform(X[:,2])
X[:,0] = labelencoder_X.fit_transform(X[:,0])
X[:,1] = labelencoder_X.fit_transform(X[:,1])
Onehotencoder = OneHotEncoder(categorical_features = [0])
Onehotencoder2 = OneHotEncoder(categorical_features = [1])
Onehotencoder3 = OneHotEncoder(categorical_features = [2])

X = Onehotencoder.fit_transform(X).toarray()
X = Onehotencoder2.fit_transform(X).toarray()
X = Onehotencoder3.fit_transform(X).toarray()
X = X[:,1:]

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.2,random_state = 0)


from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,y_train)

y_pred = regressor.predict(X_test)

import statsmodels.api as sm



X = np.append(arr = np.ones((1338,1)).astype(int), values=X,axis=1)
X_opt = X[:,[0,1,2,3,4,5,6,7,8,9,10]]
#X_opt = X[:,[0,1,2,3,4,5,6,9,10]]
xx = X_opt.tolist()
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()

print(regressor_OLS.summary())
y_test = y_test.tolist()
x = np.linspace(50000,120000,len(y_pred))
f = plt.figure()
f.set_figwidth(20)
f.set_figheight(10)
plt.plot(x,y_test)
plt.plot(x,y_pred,'r')

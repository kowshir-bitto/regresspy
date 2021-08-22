from numpy.lib.npyio import load
import numpy as np
import math
from sklearn.linear_model import SGDRegressor
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from regresspy.regression import Regression
from regresspy.loss import rmse



iris = load_iris()

X = iris.data[:, 0].reshape(-1, 1)
Y = iris.data[:, 1].reshape(-1, 1)

X_train,X_test,y_train,y_test = train_test_split(X,Y,test_size=0.2,stratify=0)


model = SGDRegressor(learning_rate=0.001, epochs=100)
model.fit(X_train,y_train)
y_pred = model.predict(X_test,y_test)

mse = mean_squared_error(y_test , y_pred)
rmse = math. sqrt(mse)
print(rmse)


my_model = Regression(learning_rate=0.001 , epochs=100)
my_model.fit(X_train , y_train)

my_model_y_pred = my_model.predict(X_test , y_test)
my_model_rmse = rmse(y_test , my_model_y_pred)
print(my_model_rmse)

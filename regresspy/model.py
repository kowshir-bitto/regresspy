

from sklearn.linear_model import SGDRegressor
from sklearn.datasets import load_iris
from regresspy.regression import Regression
from regresspy.loss import rmse
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


stochastic_gradient_descent = SGDRegressor(max_iter= 100, learning_rate= 'constant', eta0= 0.001)
stochastic_gradient_descent.fit(X, Y.reshape(-1))
sto_chas_grad_prediction = stochastic_gradient_descent.predict(X)
sto_chas_grad_rmse = rmse(sto_chas_grad_prediction, Y)
print('Stochastic Gradient Descent Regressor RMSE value:', str(sto_chas_grad_rmse))


regression_value = Regression(epochs= 100, learning_rate= 0.0001)
regression_value.fit(X, Y)
reg_pred = regression_value.predict(X)

regression_rmse = regression_value.score(reg_pred, Y)
print('RMSE value of class: ', str(regression_rmse))

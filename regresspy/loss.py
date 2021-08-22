import numpy as np
from numpy import ndarray
from math import sqrt


def mae(pred: ndarray, label: ndarray) -> ndarray:
    """Returns the mean absolute error between the predicted values and the
    actual values.

    Args:
        pred (ndarray): the array of predicted values.
        label (ndarray): the array of ground truths.
    Returns:
        (ndarray): mean absolute errors.
    """
    return np.sum(np.abs(pred-label))/pred.shape[0]


def sse(pred: ndarray, label: ndarray) -> ndarray:
    """Returns the residual sum of squared errors between the predicted
    values and the actual values.

    Args:
        pred (ndarray): the array of predicted values.
        label (ndarray): the array of ground truths.
    Returns:
        (ndarray): residual sum of squared errors.
    """
    return np.square(np.sum((pred - label)))


def mse(pred: ndarray, label: ndarray) -> ndarray:
    """Returns the mean squared errors between the predicted
    values and the actual values.

    Args:
        pred (ndarray): the array of predicted values.
        label (ndarray): the array of ground truths.
    Returns:
        (ndarray): mean squared errors.
    """
    return np.square(pred - label).mean()


def rmse(pred: ndarray, label: ndarray) -> float:
    """Returns the root mean squared error between the predicted values
    and the actual values.

    Args:
        pred (ndarray): the array of predicted values.
        label (ndarray): the array of ground truths.
    Returns:
        (ndarray): root mean squared errors.
    """
    return sqrt(np.square(pred - label).mean())

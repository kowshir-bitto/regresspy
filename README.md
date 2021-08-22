# Regresspy 
[![image](https://img.shields.io/pypi/v/py-package-template.svg)](#)
[![Build Status](https://travis-ci.org/AlexIoannides/py-package-template.svg?branch=master)](#)

A python library to implement regression model using Gradient Descent from scratch.

The regress_py package allows users to download the contents of this [GiHub repository](https://github.com/kowshir-bitto/regresspy/tree/kowshir-bitto),  containing a Regression Evaluating Python package project to be used as a gradient descent, loss and regression problem for kick-starting Machine learning or Deep Learning algorithm model evaluation of **any** type of Package; destined for upload to just for local install using Pip. The downloaded package includes the following components to measure or evalute the loss or any kind of measurement without having to spend time cloning existing set-ups from other projects:

- a minimal `setup.py` file
- testing with PyTest
- Evaluate the gradient descent loss and info

A description of how to work with (and modify) each of these components, is provided in more detail in the sections that follow-on below, as well as in the documentation and within the example code bundled with the package.

This is obviously a opinionated view of how a Python package project ought to be structured, based largely on my own experiences and requirements.



## Downloading Package

To down load the latest version of this project located in [this GiHub repository](https://github.com/kowshir-bitto/regresspy/tree/kowshir-bitto), execute the following command from the command line:

```bash
pip install regresspy
```

This will be downloaded to the current directory and will contain the following directory structure:

```bash
regress_py_package/

 |-- regresspy/
 |-- |-- __init__.py
 |-- |-- gradient_descent.py
 |-- |-- loss.py
 |-- |-- regression.py
 |-- test/
 |-- |   __init__.py
 |-- |   model.py
 |-- |   test.py
 |-- README.md
 |-- requirements.txt
 |-- setup.py
```
## Installing

Install and update using [pip](https://pip.pypa.io/en/stable/quickstart/):

```bash
pip install wheel
```
Wheel will build the package. and after that run: 

```bash
python setup.py bdist_wheel
python setup.py sdist bdist_wheel

```
It will create 2 new directory which is called build and dist. Inside of dist folder there will found a wheel file. After run this command:
```bash
pip install .\regresspy-0.2.0-py3-none-any.whl
```
## Test Package

You can also check the liner regression trained rmse value from scikitlearn and also can observe loss values according to the epochs. You can also check your train rmse according to my code. To check the model.py, open powershell and run this code:

```bash
python model.py
```
You can also test different kind of loss such as  mae, sse, mse, rmse. For this just run the below code: 
```bash
python test_loss.py
```

## How Gradient Descent Works
Gradient descent is an iterative optimization technique for determining a function's local minimum. To use gradient descent to determine a function's local minimum, we must take steps proportional to the negative of the function's gradient (move away from the gradient) at the present location.

## Step 1 
(Error function declaration) I used mae,sse,mse & rmse as error function to evaluate my model. You can find all function on loss.py file from regresspy main directory.

## Step 2 
(Forward & Bacward propagation) Forward Propagation is the way to move from the Input layer (left) to the Output layer (right) in the neural network. The process of moving from the right to left i.e backward from the Output to the Input layer is called the Backward Propagation. I declared those functions on gradient_descent.py file.

## Step 3
(Testing file creation) I used test_loss.py file to assert error functions on from my loss.py file. To do that I did generate dummy dataset and given a calculate value using hardcoding and then call separate function from loss.py file to see if they are working properly.

## Step 4 
(Regression class declaration) This is the heart of this library, all functions like train,fit,predict,score,initialize_weights are declared in a single class called Regression(). Point to be noted, we will use this function to be called on model.py file to run and see if our Regression class is working fine.

## Step 5 
(Running the model) If Regression class is the heart of this programme then this model.py file is the brain. In this case I called a scikit learn library and calculate rmse from there, in the mean time I called my Regression model and then calculate rmse using our own model that we built. Result were quit similar and package is ready.

## Conclusion 
It was an excellent software that I wrote as part of my academic career. Special thanks to my course instructor "Musabbir Hasan Sammak," who aided me much by explaining the fundamental structure of this package and correcting errors when I was completely stumped by a crucial issue in the model.py file.

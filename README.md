# Regression Evaluating Package 

[![image](https://img.shields.io/pypi/v/py-package-template.svg)](#)
[![Build Status](https://travis-ci.org/AlexIoannides/py-package-template.svg?branch=master)](#)

The regress_py package allows users to download the contents of this [GiHub repository](https://github.com/kowshir-bitto/regresspy/tree/kowshir-bitto),  containing a Regression Evaluating Python package project to be used as a gradient descent, loss and regression problem for kick-starting Machine learning or Deep Learning algorithm model evaluation of **any** type of Package; destined for upload to just for local install using Pip. The downloaded package includes the following components to measure or evalute the loss or any kind of measurement without having to spend time cloning existing set-ups from other projects:

- a minimal `setup.py` file;
- testing with PyTest;
- Evaluate the gradient descent loss and info; 

A description of how to work with (and modify) each of these components, is provided in more detail in the sections that follow-on below, as well as in the documentation and within the example code bundled with the package.

This is obviously a opinionated view of how a Python package project ought to be structured, based largely on my own experiences and requirements.



## Downloading a regress_py package

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
## Test the regress_py_package

You can also check the liner regression trained rmse value from scikitlearn and also can observe loss values according to the epochs. You can also check your train rmse according to my code. To check the model.py, open powershell and run this code:

```bash
python model.py
```
You can also test different kind of loss such as  mae, sse, mse, rmse. For this just run the below code: 
```bash
python test_loss.py
```

Now just declare the parameters and test your values.

Done! regresspy package is installed successfully. Now you can run it into your Powershell or Commandpromp.

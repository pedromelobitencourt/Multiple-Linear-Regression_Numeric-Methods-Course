# Multiple Linear Regression, Coefficient of Determination, and Residual Variance

This repository contains Python code for performing multiple linear regression, calculating the coefficient of determination (R-squared), and finding the residual variance.

## Overview

The code in this repository demonstrates how to perform multiple linear regression using Python. It takes three sets of data points: `valores_x1`, `valores_x2`, and `valores_y`, where `valores_x1` and `valores_x2` are independent variables, and `valores_y` is the dependent variable. The code calculates the coefficients for the linear regression equation and then uses it to make predictions and calculate statistical measures.

## Code Explanation

The Python code in this repository does the following:

1. Calculates the coefficients for the multiple linear regression equation.
2. Constructs the linear regression equation in the form Y(h, w) = a + b1*x1 + b2*x2.
3. Makes a prediction using the regression equation for a given set of input values (1.9 for x1 and 82 for x2).
4. Calculates the residual variance (SIGMA^2).
5. Calculates the coefficient of determination (R-squared).

## Usage

You can use this code by following these steps:

1. Clone the repository to your local machine:

```git clone <repository_url>```

2. Run the Python script containing the code provided in your preferred Python environment.

```python multiple_linear_regression.py```


3. The script will output the regression equation, a prediction for a specific input, the residual variance, and the coefficient of determination.

## Dependencies

This code uses the following Python libraries:

- NumPy

Make sure you have NumPy installed in your Python environment. You can install it using pip:

```pip install numpy```

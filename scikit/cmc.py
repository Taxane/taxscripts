#!/usr/bin/env python3

import numpy as np
import math
import random
from matplotlib import pyplot as plt
from IPython.display import clear_output


PI = 3.1415926535
e = 2.71828

def get_rand_number(min_value, max_value):
	'''
	This function gets a random number from a uniform distribution between
	the two input values [min_value, max_value] inclusively
	Args:
	- min_value (float)
	- max_value (float)
	Return:
	- Randoum number between this range (float)
	'''

	range = max_value - min_value
	choice = random.uniform(0, 1)
	return min_value + range*choice


def f_of_x(x):
	'''
	This is the main function we want to integrate over.
	Args:
	- x (float) : input to function; must be in radians
	Return:
	- output of function f(x) (float)
	'''
	return (e**(-1*x))/(1+(x-1)**2)

def crude_monte_carlo(num_samples=5000):
	'''
	This function performs the Crude Monte Carlo for our
	specific function f(x) on the range x=0 to x=5.
	Notice that this bound is sufficient because f(x)
	approaches 0 at around PI
	Args:
	- num_samples (float) : number of samples
	Return:
	- Crude Monte Carlo Estimation (float)

	'''

	lower_bound = 0
	upper_bound = 5

	sum_of_samples = 0
	for i in range(num_samples):
		x = get_rand_number(lower_bound, upper_bound)
		sum_of_samples += f_of_x(x)

	return (upper_bound - lower_bound * float(sum_of_samples/num_samples))	 

if __name__ == '__main__':
	print(crude_monte_carlo())

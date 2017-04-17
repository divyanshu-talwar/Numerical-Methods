from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
import sys
import sympy as sp
from math import exp, tan

max_val = 2
initial_x = 0
initial_y1 = 1
initial_y2 = -10
h = 0.1
n = int(max_val//h) + 1
A = [[0 for j in range(3)] for i in range(n+1)]
exact = [0 for i in range(n+1)]
error = [0 for i in range(n+1)]
A[0][0] = initial_x
A[0][1] = initial_y1
A[0][2] = initial_y2
error[0] = 0

def actual_func2(a):
	return (exp(-10*a))
def func2(a):
	return (100*a)

def main():
	global n
	global h
	global A
	global error
	global exact
	h = 0.1
	print("EULER METHOD FOR H = "+str(h))
	print("====================================")
	n = int(max_val//h) + 1
	# print h
	euler_method()
	print("x                  " +"y(h=0.1)        "+"exact        "+"error(h=0.1)                  ")
	for i in range(n+1):
		print ("%10.10f" %float(A[i][0]), end = "       ")
		print ("%10.10f" %float(A[i][1]), end = "       ")
		print ("%10.10f" %float(A[i][2]), end = "       ")
		print ("%10.10f" %float(exact[i]), end = "       ")
		print ("%10.10f" %float(error[i]), end = "       ")
		print()
	h = 0.2
	print()
	print("EULER METHOD FOR H = "+str(h))
	print("====================================")
	n = int(max_val//h) + 1
	A = [[0 for j in range(3)] for i in range(n+1)]
	A[0][0] = initial_x
	A[0][1] = initial_y1
	A[0][2] = initial_y2
	exact = [0 for i in range(n+1)]
	error = [0 for i in range(n+1)]
	euler_method()
	print("x                  " +"y(h=0.2)        "+"exact        " +"error(h=0.2)                  ")
	for i in range(n+1):
		print ("%10.10f" %float(A[i][0]), end = "       ")
		print ("%10.10f" %float(A[i][1]), end = "       ")
		print ("%10.10f" %float(A[i][2]), end = "       ")
		print ("%10.10f" %float(exact[i]), end = "       ")
		print ("%10.10f" %float(error[i]), end = "       ")
		print()

	h = 0.1
	print()
	print("BACKWARD EULER METHOD FOR H = "+str(h))
	print("====================================")
	n = int(max_val//h) + 1
	exact = [0 for i in range(n+1)]
	A = [[0 for j in range(3)] for i in range(n+1)]
	A[0][0] = initial_x
	A[0][1] = initial_y1
	A[0][2] = initial_y2
	error = [0 for i in range(n+1)]
	# print h
	backward_euler_method()
	print("Can't solve using this step size since the augmented matrix of the resultant equations is singular")
	# print("x                  " +"y(h=0.1)        "+"exact        " +"error(h=0.1)                  ")
	# for i in range(n+1):
	# 	print ("%10.10f" %float(A[i][0]), end = "       ")
	# 	print ("%10.10f" %float(A[i][1]), end = "       ")
	# 	print ("%10.10f" %float(A[i][2]), end = "       ")
	# 	print ("%10.10f" %float(exact[i]), end = "       ")
	# 	print ("%10.10f" %float(error[i]), end = "       ")
	# 	print()

	h = 0.2
	print()
	print("BACKWARD EULER METHOD FOR H = "+str(h))
	print("====================================")
	n = int(max_val//h) + 1
	exact = [0 for i in range(n+1)]
	A = [[0 for j in range(3)] for i in range(n+1)]
	A[0][0] = initial_x
	A[0][1] = initial_y1
	A[0][2] = initial_y2
	error = [0 for i in range(n+1)]
	# print h
	backward_euler_method()
	print("x                  " +"y(h=0.2)        " +"exact        "+"error(h=0.2)                  ")
	for i in range(n+1):
		print ("%10.10f" %float(A[i][0]), end = "       ")
		print ("%10.10f" %float(A[i][1]), end = "       ")
		print ("%10.10f" %float(A[i][2]), end = "       ")
		print ("%10.10f" %float(exact[i]), end = "       ")
		print ("%10.10f" %float(error[i]), end = "       ")
		print()


def euler_method():
	for i in range(n):
		b1 = A[i][2]
		b2 = func2(A[i][1])
		A[i+1][0] = A[i][0] + h
		A[i+1][1] = A[i][1] + h*b1
		A[i+1][2] = A[i][2] + h*b2
	for i in range(n+1):
		exact[i] = actual_func2(A[i][0])
		error[i] = actual_func2(A[i][0]) - A[i][1]

def backward_euler_method():
	for i in range(n):
		A[i+1][0] = A[i][0] + h
		A[i+1][1] = (A[i][1] + h*A[i][2])/(1 - 100*(h**2))
		A[i+1][2] = A[i][2] + 100*h*A[i+1][1]

	for i in range(n+1):
		exact[i] = actual_func2(A[i][0])
		error[i] = actual_func2(A[i][0]) - A[i][1]

main()


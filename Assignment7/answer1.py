from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
import sys
import sympy as sp
from math import exp, tan

max_val = 1
initial_x = 0
initial_y = 0
h = 0.1
n = int(max_val//h) + 1
A = [[0 for j in range(2)] for i in range(n+1)]
error = [0 for i in range(n+1)]
exact = [0 for i in range(n+1)]
A[0][0] = initial_x
A[0][1] = initial_y
error[0] = 0


def actual_func1(a):
	return (tan(a) - a)
def func1(a, b):
	return ((a + b)**2)

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
		print ("%10.7f" %float(A[i][0]), end = "       ")
		print ("%10.7f" %float(A[i][1]), end = "       ")
		print ("%10.7f" %float(exact[i]), end = "       ")
		print ("%10.7f" %float(error[i]), end = "       ")
		print()
	h = 0.05
	print("EULER METHOD FOR H = "+str(h))
	print("====================================")
	n = int(max_val//h) + 1
	exact = [0 for i in range(n+1)]
	A = [[0 for j in range(2)] for i in range(n+1)]
	A[0][0] = initial_x
	A[0][1] = initial_y
	error = [0 for i in range(n+1)]
	euler_method()
	print("x                  " +"y(h=0.05)        "+"exact        " +"error(h=0.05)                  ")
	for i in range(n+1):
		print ("%10.7f" %float(A[i][0]), end = "       ")
		print ("%10.7f" %float(A[i][1]), end = "       ")
		print ("%10.7f" %float(exact[i]), end = "       ")
		print ("%10.7f" %float(error[i]), end = "       ")
		print()

	h = 0.1
	print("IMPROVED EULER METHOD FOR H = "+str(h))
	print("====================================")
	n = int(max_val//h) + 1
	exact = [0 for i in range(n+1)]
	A = [[0 for j in range(2)] for i in range(n+1)]
	A[0][0] = initial_x
	A[0][1] = initial_y
	error = [0 for i in range(n+1)]
	# print h
	improved_euler_method()
	print("x                  " +"y(h=0.1)        "+"exact        " +"error(h=0.1)                  ")
	for i in range(n+1):
		print ("%10.7f" %float(A[i][0]), end = "       ")
		print ("%10.7f" %float(A[i][1]), end = "       ")
		print ("%10.7f" %float(exact[i]), end = "       ")
		print ("%10.7f" %float(error[i]), end = "       ")
		print()
	h = 0.05
	print("IMPROVED EULER METHOD FOR H = "+str(h))
	print("====================================")
	n = int(max_val//h) + 1
	exact = [0 for i in range(n+1)]
	A = [[0 for j in range(2)] for i in range(n+1)]
	A[0][0] = initial_x
	A[0][1] = initial_y
	error = [0 for i in range(n+1)]
	improved_euler_method()
	print("x                  " +"y(h=0.1)        "+"exact        " +"error(h=0.05)                  ")
	for i in range(n+1):
		print ("%10.7f" %float(A[i][0]), end = "       ")
		print ("%10.7f" %float(A[i][1]), end = "       ")
		print ("%10.7f" %float(exact[i]), end = "       ")
		print ("%10.7f" %float(error[i]), end = "       ")
		print()

def euler_method():
	for i in range(n):
		b = func1(A[i][0], A[i][1])
		A[i+1][0] = A[i][0] + h
		A[i+1][1] = A[i][1] + h*b
	for i in range(n+1):
		exact[i] = actual_func1(A[i][0])
		error[i] = actual_func1(A[i][0]) - A[i][1]

def improved_euler_method():
	for i in range(n):
		b1 = func1(A[i][0], A[i][1])
		A[i+1][0] = A[i][0] + h
		t = A[i][1] + h*b1
		b2 = func1(A[i+1][0], t)
		A[i+1][1] = A[i][1] + 0.5*h*(b1+b2)
	for i in range(n+1):
		exact[i] = actual_func1(A[i][0])
		error[i] = actual_func1(A[i][0]) - A[i][1]

main()


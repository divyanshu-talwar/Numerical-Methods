from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
import sys
import sympy as sp
from math import exp, tan

max_val = 2
initial_x = 0
initial_y = 1
h = 0.19
n = int(max_val//h) + 1
A = [[0 for j in range(2)] for i in range(n+1)]
exact = [0 for i in range(n+1)]
error = [0 for i in range(n+1)]
A[0][0] = initial_x
A[0][1] = initial_y
error[0] = 0

def actual_func2(a):
	return (exp(-10*a))
def func2(a):
	return (-10*a)

def main():
	global n
	global h
	global A
	global error
	global exact
	h = 0.19
	print("EULER METHOD FOR H = "+str(h))
	print("====================================")
	n = int(max_val//h) + 1
	# print h
	x_val = [0 for i in range(n+1)]
	y_val = [0 for i in range(n+1)]
	euler_method()
	print("x                  " +"y(h=0.19)        "+"exact        "+"error(h=0.19)                  ")
	for i in range(n+1):
		x_val[i] = A[i][0]
		y_val[i] = A[i][1]
		print ("%10.10f" %float(A[i][0]), end = "       ")
		print ("%10.10f" %float(A[i][1]), end = "       ")
		print ("%10.10f" %float(exact[i]), end = "       ")
		print ("%10.10f" %float(error[i]), end = "       ")
		print()

	plt.plot( x_val, y_val,'r--',label = "euler method h=0.19",linewidth=1.5)
	plt.plot(x_val, y_val,  'mo')
	h = 0.2
	print()
	print("EULER METHOD FOR H = "+str(h))
	print("====================================")
	n = int(max_val//h) + 1
	A = [[0 for j in range(2)] for i in range(n+1)]
	A[0][0] = initial_x
	A[0][1] = initial_y
	x_val = [0 for i in range(n+1)]
	y_val = [0 for i in range(n+1)]
	exact = [0 for i in range(n+1)]
	error = [0 for i in range(n+1)]
	euler_method()
	print("x                  " +"y(h=0.2)        "+"exact        " +"error(h=0.2)                  ")
	for i in range(n+1):
		x_val[i] = A[i][0]
		y_val[i] = A[i][1]
		print ("%10.10f" %float(A[i][0]), end = "       ")
		print ("%10.10f" %float(A[i][1]), end = "       ")
		print ("%10.10f" %float(exact[i]), end = "       ")
		print ("%10.10f" %float(error[i]), end = "       ")
		print()
	plt.plot( x_val, y_val,'c--',label = "euler method h=0.20",linewidth=1.5)
	plt.plot(x_val, y_val,  'go')
	h = 0.21
	print()
	print("EULER METHOD FOR H = "+str(h))
	print("====================================")
	n = int(max_val//h) + 1
	A = [[0 for j in range(2)] for i in range(n+1)]
	A[0][0] = initial_x
	A[0][1] = initial_y
	x_val = [0 for i in range(n+1)]
	y_val = [0 for i in range(n+1)]
	exact = [0 for i in range(n+1)]
	error = [0 for i in range(n+1)]
	# print h
	print(n)
	euler_method()
	print("x                  " +"y(h=0.21)        "+"exact        " +"error(h=0.21)                  ")
	for i in range(n+1):
		x_val[i] = A[i][0]
		y_val[i] = A[i][1]
		print ("%10.10f" %float(A[i][0]), end = "       ")
		print ("%10.10f" %float(A[i][1]), end = "       ")
		print ("%10.10f" %float(exact[i]), end = "       ")
		print ("%10.10f" %float(error[i]), end = "       ")
		print()
	plt.plot( x_val, y_val,'r-.',label = "euler method h=0.21",linewidth=1.5)
	plt.plot(x_val, y_val,  'bo')
	h = 0.2
	print()
	print("BACKWARD EULER METHOD FOR H = "+str(h))
	print("====================================")
	n = int(max_val//h) + 1
	exact = [0 for i in range(n+1)]
	x_val = [0 for i in range(n+1)]
	y_val = [0 for i in range(n+1)]
	A = [[0 for j in range(2)] for i in range(n+1)]
	A[0][0] = initial_x
	A[0][1] = initial_y
	error = [0 for i in range(n+1)]
	# print h
	backward_euler_method()
	print("x                  " +"y(h=0.2)        "+"exact        " +"error(h=0.2)                  ")
	for i in range(n+1):
		x_val[i] = A[i][0]
		y_val[i] = A[i][1]
		print ("%10.10f" %float(A[i][0]), end = "       ")
		print ("%10.10f" %float(A[i][1]), end = "       ")
		print ("%10.10f" %float(exact[i]), end = "       ")
		print ("%10.10f" %float(error[i]), end = "       ")
		print()

	plt.plot( x_val, y_val,'b--',label = "back_euler method h=0.2",linewidth=1.5)
	plt.plot(x_val, y_val,  'go')
	h = 0.3
	print()
	print("BACKWARD EULER METHOD FOR H = "+str(h))
	print("====================================")
	n = int(max_val//h) + 1
	exact = [0 for i in range(n+1)]
	A = [[0 for j in range(2)] for i in range(n+1)]
	x_val = [0 for i in range(n+1)]
	y_val = [0 for i in range(n+1)]
	A[0][0] = initial_x
	A[0][1] = initial_y
	error = [0 for i in range(n+1)]
	# print h
	backward_euler_method()
	print("x                  " +"y(h=0.3)        " +"exact        "+"error(h=0.3)                  ")
	for i in range(n+1):
		x_val[i] = A[i][0]
		y_val[i] = A[i][1]
		print ("%10.10f" %float(A[i][0]), end = "       ")
		print ("%10.10f" %float(A[i][1]), end = "       ")
		print ("%10.10f" %float(exact[i]), end = "       ")
		print ("%10.10f" %float(error[i]), end = "       ")
		print()
	plt.plot( x_val, y_val,'m--',label = "back_euler method h=0.3",linewidth=1.5)
	plt.plot(x_val, y_val,  'bo')
	plot('g',"exp(-10*t) - actual", -0.15, 2.5, 1)
	plt.xlabel("X - Axis")
	plt.ylabel("Y - Axis")
	plt.xlim(-0.5,2.5)
	# plt.ylim(-0.5,1.5)
	plt.legend(loc='upper left',numpoints = 1)
	plt.show()

def plot(color,la,l,u,w):
	t = np.arange(l,u,0.01)
	y = [ (actual_func2(i)) for i in t]
	plot = plt.plot( t, y,color,label = la,linewidth=w)

def euler_method():
	for i in range(n):
		b = func2(A[i][1])
		A[i+1][0] = A[i][0] + h
		A[i+1][1] = A[i][1] + h*b
	for i in range(n+1):
		exact[i] = actual_func2(A[i][0])
		error[i] = actual_func2(A[i][0]) - A[i][1]

def backward_euler_method():
	for i in range(n):
		A[i+1][0] = A[i][0] + h
		A[i+1][1] = A[i][1]/(1+10*h)
	for i in range(n+1):
		exact[i] = actual_func2(A[i][0])
		error[i] = actual_func2(A[i][0]) - A[i][1]

main()


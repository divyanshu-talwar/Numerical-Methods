from __future__ import print_function
import numpy as np
import sympy as sp
import math
import matplotlib.pyplot as plt
no_of_pts = input()
x = sp.Symbol('x')
datapoints = [[0.0 for i in range(2)] for j in range(no_of_pts)]
linear = [0.0 for i in range(2)]
quadratic = [0.0 for i in range(3)]
cubic = [0.0 for i in range(4)]  
t = no_of_pts
xi = 0
yi = 0
xi_2 = 0
xi_3 = 0
xi_4 = 0
xi_5 = 0
xi_6 = 0
xi_yi = 0
xi2_yi = 0
xi3_yi = 0

def main():
	for k in range(no_of_pts):
		n = raw_input()
		n = n.split(" ");
		datapoints[k][0] = eval(n[0])
		datapoints[k][1] = eval(n[1])
	t = no_of_pts
	global xi
	global yi
	global xi_2
	global xi_3
	global xi_4
	global xi_5
	global xi_6
	global xi_yi
	global xi2_yi
	global xi3_yi
	for k in range(no_of_pts):
		xi += datapoints[k][0]
		yi += datapoints[k][1]
		xi_2 += datapoints[k][0]**2
		xi_3 += datapoints[k][0]**3
		xi_4 += datapoints[k][0]**4
		xi_5 += datapoints[k][0]**5
		xi_6 += datapoints[k][0]**6
		xi_yi += datapoints[k][0]*datapoints[k][1]
		xi2_yi += (datapoints[k][0]**2)*datapoints[k][1]
		xi3_yi += (datapoints[k][0]**3)*datapoints[k][1]
	curve_fitting()
	f1 = linear[0] + linear[1]*x
	f2 = quadratic[0] + quadratic[1]*x + quadratic[2]*x**2
	f3 = cubic[0] + cubic[1]*x + cubic[2]*x**2 + cubic[3]*x**3
	print("linear : " + str(f1))
	print("quadratic : " + str(f2))
	print("cubic : " + str(f3))
	plot(f1,'r',"linear",-4.5,4.5,1.0)
	plot(f2,'b:',"quadratic",-4.5,4.5,5.0)
	plot(f3,'g--',"cubic",-4.5,4.5,1.5)
	x_list = []
	y_list = []
	for x_p, y_p in datapoints:
		x_list.append(x_p)
		y_list.append(y_p)
	plt.plot(x_list, y_list,  'ro',label = "data points")
	plt.xlabel("X - Axis")
	plt.ylabel("Y - Axis")
	plt.xlim(-4.5,4.5)
	plt.ylim(-1,1.3)
	plt.legend(loc='upper left',numpoints = 1)
	plt.show()


def curve_fitting():
	global linear
	global quadratic
	global cubic
	l_lhs = [[t,xi],[xi,xi_2]]
	l_rhs = np.array([yi,xi_yi])
	linear = np.linalg.solve(l_lhs, l_rhs)
	q_lhs = [[t,xi,xi_2],[xi,xi_2,xi_3],[xi_2,xi_3,xi_4]]
	q_rhs = np.array([yi,xi_yi,xi2_yi])
	quadratic = np.linalg.solve(q_lhs, q_rhs)
	c_lhs = [[t,xi,xi_2,xi_3],[xi,xi_2,xi_3,xi_4],[xi_2,xi_3,xi_4,xi_5],[xi_3,xi_4,xi_5,xi_6]]
	c_rhs = np.array([yi,xi_yi,xi2_yi,xi3_yi])
	cubic = np.linalg.solve(c_lhs, c_rhs)
	print(cubic)
	print(quadratic)

def plot(f,color,la,l,u,w):
	global max_y
	t = np.arange(l,u,0.01)
	y = [ f.evalf(subs = {x:i}) for i in t]
	plot = plt.plot( t, y,color,label = la,linewidth=w)

main()
import numpy as np
import matplotlib.pyplot as plt
import sys
import sympy as sp

x = sp.Symbol('x')
points = [(0,1),(1,0.765198),(2,0.223891),(3,-0.260052)]
l = ["L0","L1","L2","L3"]
n = len(points)

def main():
	P = lagrange()
	color = ['b','g','r','m','c']
	for i in range(4):
		Li = sp.simplify(g(i))
		print("L"+str(i)+" : " + str(sp.expand(Li)))
		plot(Li,color[i],l[i])

	print("P3(x) : " + str(sp.expand(P)))
	plot(P,color[4],"p3(x)")

	x_list = []
	y_list = []
	for x_p, y_p in points:
		x_list.append(x_p)
		y_list.append(y_p)
	plt.plot(x_list, y_list,  'ro',label = "data points")

	plt.xlabel("X - Axis")
	plt.ylabel("Y - Axis")
	plt.xlim(-1, 4)
	plt.ylim(-2, 4)
	plt.legend(loc='upper center',numpoints = 1)
	plt.show()
	

def plot(f,color,la):
	t = np.arange(-1,4,0.01)
	y = [ f.evalf(subs = {x:i}) for i in t]
	plot = plt.plot( t, y,color,label = la,linewidth=1.5)

def g(i):			
	tot_mul = 1
	for j in xrange(n):
		if i != j:
			xj, yj = points[j]
			tot_mul *= (x - xj) / float(points[i][0] - xj)
		
	return tot_mul

def lagrange():
	total = 0
	for i in xrange(n):
		total += points[i][1] * g(i)
	total = (sp.simplify(total))
	return total

main()
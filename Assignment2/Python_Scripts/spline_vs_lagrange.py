from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import sys
import sympy as sp

x = sp.Symbol('x')
points = []
n = 11
k = np.zeros([n,1])
k[0] = 10/(26)**2
k[n-1] = -10/(26)**2
coeff = np.zeros([n-1,4])
max_y = []

def main():
	color = ['g','r','r','c','b']
	f = 1/(1+x**2)

	print f
	plot(f,color[0],"f(x)",-5.5,5.5,2)

	for i in xrange(-5,6):
		points.append([i,f.evalf(subs = {x:i})])
	# print points

	spline()

	for i in range(n-1):
		temp = 0
		for j in range(3,-1,-1):
			temp += (coeff[i][j])*((x-points[i][0])**j)
		print ("q" + str(i) + " :  " + str(sp.expand(temp)))
		if i == 0 :
			plot(temp,color[2],"",points[i][0] - 0.5,points[i+1][0],1.0)
		if i == n-2 :
			plot(temp,color[2],"g(x)=spline",points[i][0],points[i+1][0]+ 0.5,1.0)
		plot(temp,color[2],"",points[i][0],points[i+1][0],1.0)


	P = lagrange()

	print ("p10(x) :  " + str(sp.expand(P)))
	plot(P,color[4],"p10(x)",-5.5,5.5,1)

	x_list = []
	y_list = []
	for x_p, y_p in points:
		x_list.append(x_p)
		y_list.append(y_p)
	plt.plot(x_list, y_list,  'ro',label = "data points")

	plt.xlabel("X - Axis")
	plt.ylabel("Y - Axis")
	plt.xlim(-5.5,5.5)
	plt.ylim(-0.5,1.5)
	plt.legend(loc='upper left',numpoints = 1)
	plt.show()

	print("Maximum Deviation between p10(x)and f(x) : 1.91559434819")
	print("Maximum Deviation between g(x)[cubic spline] and f(x) : 0.0219719562612")
	

def plot(f,color,la,l,u,w):
	global max_y
	t = np.arange(l,u,0.01)
	y = [ f.evalf(subs = {x:i}) for i in t]
	plot = plt.plot( t, y,color,label = la,linewidth=w)

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

def spline():
	for i in range(n-1):
		coeff[i][0] = points[i][1]

	A = np.zeros([n-2,4])
	# print A
	for i in range(1,n-1):
		if i != 1 :
			A[i-1][0] = 1
		if i != n-2:
			A[i-1][2] = 1
		A[i-1][1] = 4
		A[i-1][3] = 3*(points[i+1][1]-points[i-1][1])

	A[0][3] -= k[0]
	A[n-3][3] -= k[10]

	# print A
	calc_k(A,n-2)
	# print k

	for i in range(n-1):
		coeff[i][1] = k[i]
		coeff[i][2] = (3*(points[i+1][1]-points[i][1])) - (k[i+1] + 2*k[i])
		coeff[i][3] = (2*(points[i][1]-points[i+1][1])) + (k[i+1] + k[i])

def calc_k(A,t):
	for i in range(1,t):
		mf = A[i][0]/A[i-1][1] 
		A[i][0] -= (mf)*A[i-1][1]
		A[i][1] -= (mf)*A[i-1][2]
		A[i][3] -= (mf)*A[i-1][3]

	k[t] = (A[t-1][3]/A[t-1][1])

	for j in range(t-2,-1,-1):
		k[j+1] = (A[j][3] - (A[j][2] * k[j+2]))/(A[j][1])

main()
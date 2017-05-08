
from __future__ import division
import numpy
from sympy import *
import matplotlib.pyplot as plt
import math
import numpy

time = [0, 0.02, 0.04, 0.06, 0.08, 0.10, 0.12, 0.14, 0.16, 0.18, 0.20]
pos = [0, 0.2, 0.4, 0.6, 0.8, 1.0]

def customRange(x,y,step):
	while(x<y):
		yield x
		x += step

def triadiagonalizeMatrix(r, n, augmentedValues, count1, anotherMatrix):
	global time, pos
	augmentedValues = list(augmentedValues)
	diagonal = [1] + [2+(2*r)]*(n-2) + [1]
	aboveDiagonal = [0] + [-r]*(n-1)
	belowDiagonal = [-r]*(n-1) + [0]
	for i in range(1,n):
		multiplicationFactor = belowDiagonal[i]/diagonal[i-1]
		belowDiagonal[i] -= multiplicationFactor*diagonal[i-1]
		diagonal[i] -= multiplicationFactor*aboveDiagonal[i-1]
		augmentedValues[i] -= multiplicationFactor*augmentedValues[i-1]
	x9 = augmentedValues[n-1]/diagonal[n-1]	
	x = []
	x.append(x9)
	count = 0
	for i in range(n-2,-1,-1):
		x.append((augmentedValues[i] - aboveDiagonal[i]*x[count])/diagonal[i])
		count += 1
	x = x[::-1]
	x = numpy.concatenate(x).ravel().tolist()
	color = ['g', 'r', 'b', 'm', 'y', 'k', 'c', "chocolate", "brown", "crimson", "olive"]
	plt.plot( pos, x[0], color[count1], label = "value at t = {val}".format(val = time[count1]), linewidth = 1.5)
	plt.plot(pos, x[0],  'go')
	print "The solution for time = {value} is as follows :-\n".format(value = time[count1])
	for i in range(len(x[0])):
		print "Log position[{i}] temperature value = {value}".format(i = pos[i], value = x[0][i])
	print
	# print(x)
	augmentedValues = numpy.array(x).reshape((6,1))
	augmentedValues = numpy.matrix(augmentedValues)
	augmentedValues = anotherMatrix * augmentedValues
	# print(augmentedValues)
	return augmentedValues

def exact(n, l, deltaX, deltaT):
	global time, pos
	color = ['g--', 'r--', 'b--', 'm--', 'y--', 'k--', 'c--', "chocolate", "brown", "crimson", "olive"]
	x = Symbol('x')
	t = Symbol('t')
	function = sin(pi*x)*(E**(-1*(t)*(pi**2)))
	for j in range(len(time)):
		if(j==0):
			a = numpy.arange(0,2,0.01)
		else:
			a = numpy.arange(0,5,0.01)
		y = [ function.evalf(subs = {x:i,t:time[j]}) for i in a]
		plot = plt.plot( a, y,color[j],label = "exact at t = {val}".format(val = time[j]),linewidth = 1, linestyle = '--')
	count = 0
	for i in customRange(0,0.204,deltaT):
		temp = []
		for j in customRange(0,l+deltaX,deltaX):
			temp.append(function.evalf(subs={x:j, t:i}))
		print "The exact solution for time = {value} is as follows :-\n".format(value = time[count])
		for k in range(len(temp)):
			print "Log position[{i}] = {value}".format(i = pos[k], value = temp[k])
		count += 1
		print

def main():
	global pos, time
	alpha = 1
	l = 1
	deltaX = 0.2
	deltaT = 0.04 # check again
	r = (alpha*deltaT)/((deltaX**2)*2)
	n = len(pos) # check again
	augmentedValues = []
	x = Symbol('x')
	function = sin(pi*x)
	print(r)

	# numpy.diagflat([-sigma_u for i in range(J-1)], -1) +\
 #      numpy.diagflat([1.+sigma_u]+[1.+2.*sigma_u for i in range(J-2)]+[1.+sigma_u]) +\
 #      numpy.diagflat([-sigma_u for i in range(J-1)], 1)


	A_u = numpy.diagflat([r for i in range(n-1)], -1) + numpy.diagflat([1.+0] + [2.-2.*r for i in range(n-2)]+ [1.+0]) + numpy.diagflat([r for i in range(n-1)], 1)
	for i in range(6):
		for j in range(6):
			if( i == 0 and j == 1 ):
				A_u[i][j] = 0
			elif( i == 5 and j == 4 ):
				A_u[i][j] = 0
	# print(A_u)
	# exit(0)
	for i in customRange(0,l+0.2,deltaX):
		augmentedValues.append(function.evalf(subs={x:i}))
	print "The solution for time = 0 is as follows :-\n"
	# initial = numpy.concatenate(augmentedValues).ravel().tolist()
	for i in range(len(augmentedValues)):
		print "Log position[{i}] temperature value = {value}".format(i = pos[i], value = augmentedValues[i])
	color = ['g', 'r', 'b', 'm', 'y', 'k', 'c', "chocolate", "brown", "crimson", "olive"]
	plt.plot( pos, augmentedValues, color[0], label = "value at t = {val}".format(val = time[0]), linewidth = 1.5)
	plt.plot(pos, augmentedValues,  'go')
	
	augmentedValues = numpy.matrix(augmentedValues).reshape((6,1))
	A_u = numpy.matrix(A_u)
	augmentedValues = A_u * augmentedValues
	# print(augmentedValues)
	count = 1
	for i in range(len(time)-1):
		augmentedValues = triadiagonalizeMatrix(r, n, augmentedValues, count, A_u)
		count += 1
	print("-------------------------------------------")
	exact(n, l, deltaX, deltaT)
	plt.xlabel("X - Axis")
	plt.ylabel("Y - Axis")
	plt.xlim(-0,1)
	plt.ylim(-0,1.5)
	legend = plt.legend(loc = 'upper left', scatterpoints = 1, bbox_to_anchor=(1, 1))
	plt.savefig("Crank Nicolson", bbox_extra_artists=(legend,), bbox_inches='tight')
	plt.show()

main()
from __future__ import division
import numpy
from sympy import *
import matplotlib.pyplot as plt
import math
import numpy as np

# time = [0, 0.04, 0.08, 0.12, 0.16, 0.20]
time = [0, 0.02, 0.04, 0.06, 0.08, 0.10, 0.12, 0.14, 0.16, 0.18, 0.20]
pos = [0, 0.2, 0.4, 0.6, 0.8, 1.0]

def customRange(x,y,step):
	while(x<y):
		yield x
		x += step

def triadiagonalizeMatrix(r, n, augmentedValues, count1):
	global time, pos
	# r = int(r)

	diagonal = [1] + [1+(2*r)]*(n-2) + [1]
	aboveDiagonal = [0] + [-r]*(n-1)
	belowDiagonal = [-r]*(n-1) + [0]
	# print(aboveDiagonal)
	# print(diagonal)
	# print(belowDiagonal)
	# exit(0)
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
	print "The solution for time = {value} is as follows :-\n".format(value = time[count1])
	for i in range(len(x)):
		print "Log position[{i}] temperature value = {value}".format(i = pos[i], value = x[i])	
	color = ['g', 'r', 'b', 'm', 'y', 'k', 'c', "chocolate", "brown", "crimson", "olive"]
	plt.plot( pos, x, color[count1],label = "value at t = {val}".format(val = time[count1]),linewidth=1.5)
	plt.plot(pos, x,  'go')
	print
	augmentedValues = x
	return augmentedValues

def exact(n, l, deltaX, deltaT):
	global time, pos
	color = ['g--', 'r--', 'b--', 'm--', 'y--', 'k--', 'c--', "chocolate", "brown", "crimson", "olive"]
	x = Symbol('x')
	t = Symbol('t')
	function = sin(pi*x)*(E**(-1*(t)*(pi**2)))
	for j in range(len(time)):
		if(j==0):
			a = np.arange(0,2,0.01)
		else:
			a = np.arange(0,5,0.01)
		y = [ function.evalf(subs = {x:i,t:time[j]}) for i in a]
		plot = plt.plot( a, y,color[j],label = "exact at t = {val}".format(val = time[j]), linewidth = 1, linestyle = '--')
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
	deltaT = 0.02 # check again
	r = ((deltaT)/(deltaX**2))*alpha
	# print(r)
	n = len(pos) # check again
	augmentedValues = []
	x = Symbol('x')
	function = sin(pi*x)
	for i in customRange(0,l,deltaX):
		augmentedValues.append(function.evalf(subs={x:i}))
	augmentedValues.append(0)
	print "The solution for time = 0 is as follows :-\n"
	for i in range(len(augmentedValues)):
		print "Log Position[{i}] = {value}".format(i = pos[i], value = augmentedValues[i])
	color = ['g', 'r', 'b', 'm', 'y', 'k', 'c', "chocolate", "brown", "crimson", "olive"]
	r = 0.5
	plt.plot( pos, augmentedValues, color[0],label = "value at t = {val}".format(val = time[0]),linewidth=1.5)
	plt.plot(pos, augmentedValues,  'go')
	count = 1
	# print(r)
	for i in range(len(time)-1):
		# print("wdonwso")
		# print(r)
		augmentedValues = triadiagonalizeMatrix(r, n, augmentedValues, count)
		count += 1
	print("-------------------------------------------")
	exact(n, l, deltaX, deltaT)
	plt.xlabel("X - Axis")
	plt.ylabel("Y - Axis")
	plt.xlim(-0,1)
	plt.ylim(-0,1.5)
	legend = plt.legend(loc = 'upper left', scatterpoints = 1, bbox_to_anchor=(1, 1))
	plt.savefig("FTCS Implicit", bbox_extra_artists=(legend,), bbox_inches='tight')
	plt.show()

main()
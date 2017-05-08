
from __future__ import division
import numpy
from sympy import *
import matplotlib.pyplot as plt
import math
import numpy as np

# time = [0, 0.04, 0.08, 0.12, 0.16, 0.20]
time = [0, 0.02, 0.04, 0.06, 0.08, 0.10, 0.12, 0.14, 0.16, 0.18, 0.20]
# time = [0, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.10, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.20]
pos = [0, 0.2, 0.4, 0.6, 0.8, 1.0]

def customRange(x,y,step):
	while(x<y):
		yield x
		x += step

def exact(n, l, deltaX, deltaT):
	global time, pos
	color = ['g--', 'r--', 'b--', 'm--', 'y--', 'k--', 'c--', "chocolate", "brown", "crimson", "olive", "aliceblue" , "burlywood" , "darksalmon", "honeydew" , "lime" , "pink" , "plum" ,
	 "springgreen", "teal" , "tan"]
	x = Symbol('x')
	t = Symbol('t')
	function = sin(pi*x)*(E**(-1*(t)*(pi**2)))
	for j in range(len(time)):
		if(j==0):
			a = np.arange(0,2,0.01)
		else:
			a = np.arange(0,5,0.01)
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
	x = Symbol('x')
	function = sin(pi*x)
	uOld = []
	inc = 1
	alpha = 1
	l = 1
	deltaX = 0.2
	deltaT = 0.02
	r = (alpha*deltaT)/(deltaX**2)
	n = len(pos)
	# print(r)
	# exit(0)
	# m = 0
	for i in customRange(0,l+0.02,deltaX):
		uOld.append(function.evalf(subs={x:i}))
	count = 0
	print "The solution for time = {value} is as follows :-\n".format(value = time[0])
	for i in uOld:
		print "Log position[{i}] = temperature value = {value}".format(i = pos[count], value = i)
		count += 1
	print
	color = ['g', 'r', 'b', 'm', 'y', 'k', 'c', "chocolate", "brown", "crimson", "olive", "aliceblue" , "burlywood" , "darksalmon", "honeydew" , "lime" , "pink" , "plum" ,
	 "springgreen", "teal" , "tan"]
	plt.plot( pos, uOld, color[0], label = "value at t = {val}".format(val = time[0]), linewidth=1.5)
	plt.plot(pos, uOld,  'go')
	for i in range(len(time)-1):
		uNew = []
		uNew.append(uOld[0])
		for j in range(1,len(uOld)-1):
			uNew.append(r*(uOld[j+1]-(2*uOld[j])+uOld[j-1]) + uOld[j])
		uNew.append(uOld[len(uOld)-1])
		# if( m == 0 ):
		# 	uNew.append(0)
		# 	m += 1
		count = 0
		print "The solution for time = {value} is as follows :-\n".format(value = time[inc])
		for i in uNew:
			print "Log position[{i}] = temperature value = {value}".format(i = pos[count], value = i)
			count += 1
		print
		# color = ['g', 'r', 'b', 'm', 'y', 'k', 'c', "chocolate", "brown", "crimson", "olive"]
		plt.plot( pos, uNew, color[inc], label = "value at t = {val}".format(val = time[inc]), linewidth=1.5)
		inc += 1
		plt.plot(pos, uNew,  'go')
		uOld = uNew
	print("-------------------------------------------")
	exact(n, l, deltaX, deltaT)
	plt.xlabel("X - Axis")
	plt.ylabel("Y - Axis")
	plt.xlim(-0,1)
	plt.ylim(-0,1.5)
	legend = plt.legend(loc = 'upper left', scatterpoints = 1, bbox_to_anchor=(1, 1))
	plt.savefig("FTCS Explicit", bbox_extra_artists=(legend,), bbox_inches='tight')
	plt.show()

main()
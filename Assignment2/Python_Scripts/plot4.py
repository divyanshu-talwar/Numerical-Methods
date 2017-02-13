import numpy as np
import matplotlib.pyplot as plt
import sys
import sympy as sp

x = sp.Symbol('x')

def main():
	q0 = 1+ (x**3)
	q1 = 9 + 12*(x-2) + 6*((x-2)**2) -2*((x-2)**3)
	q2 = 41 + 12*(x-4) -6*((x-4)**2)
	color = ['b','g','r','m','c']

	t = np.arange(0,2,0.01)
	y = [ q0.evalf(subs = {x:i}) for i in t]
	plot = plt.plot( t, y,color[0],label = "q0",linewidth=1.5)

	t = np.arange(2,4,0.01)
	y = [ q1.evalf(subs = {x:i}) for i in t]
	plot = plt.plot( t, y,color[1],label = "q1",linewidth=1.5)

	t = np.arange(4,6,0.01)
	y = [ q2.evalf(subs = {x:i}) for i in t]
	plot = plt.plot( t, y,color[3],label = "q2",linewidth=1.5)


	plt.xlabel("X - Axis")
	plt.ylabel("Y - Axis")
	plt.xlim(-0.5, 6)
	plt.legend(loc='upper center',numpoints = 1)
	plt.show()

main()
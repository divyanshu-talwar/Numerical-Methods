import numpy as np
import matplotlib.pyplot as plt
import sys
import sympy as sp

x = sp.Symbol('x')

def main():
	q0 = -(x**2)-2*(x**3)
	q1 = -(x**2) + 2*(x**3)
	p2 = (x**2)
	f = (x**4)
	color = ['b','g','r','--m','c']

	t = np.arange(-1,0,0.01)
	y = [ q0.evalf(subs = {x:i}) for i in t]
	plot = plt.plot( t, y,color[0],label = "q0",linewidth=1.5)

	t = np.arange(0,1,0.01)
	y = [ q1.evalf(subs = {x:i}) for i in t]
	plot = plt.plot( t, y,color[1],label = "q1",linewidth=1.5)

	t = np.arange(-1,1,0.01)
	y = [ p2.evalf(subs = {x:i}) for i in t]
	plot = plt.plot( t, y,color[4],label = "p2(x)",linewidth=1.5)

	t = np.arange(-1,1,0.01)
	y = [ f.evalf(subs = {x:i}) for i in t]
	plot = plt.plot( t, y,color[3],label = "f(x)",linewidth=1.5)

	plt.xlabel("X - Axis")
	plt.ylabel("Y - Axis")
	plt.xlim(-1.5, 2)
	plt.ylim(-0.5, 2)
	plt.legend(loc='upper center',numpoints = 1)
	plt.show()

main()
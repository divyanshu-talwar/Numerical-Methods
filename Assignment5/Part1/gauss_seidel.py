from __future__ import print_function
import numpy as np
import sympy as sp
import math
import matplotlib.pyplot as plt
test_cases = input()
t_overall = [0 for j in range(test_cases)]
count_overall = [0 for j in range(test_cases)]
spectral_radius = [0 for j in range(test_cases)]

def main():
	global t
	global n
	global A
	global x
	global L
	global U
	global b
	for k in range(test_cases):
		n = input()
		t = input()
		t_overall[k] = t
		print("For test case number : " + str(k+1))
		print("Value of t = " + str(t))
		A = [[0.0 for j in range(n)] for i in range(n)]
		x = [[0.0 for j in range(n)] for i in range(3)]
		L = [[0.0 for j in range(n)] for i in range(n)]
		U = [[0.0 for j in range(n)] for i in range(n)]
		b = [0.0 for j in range(n)]
		for i in range (n):
			for j in range(n):
				if(i > j):
					A[i][j] = t
					L[i][j] = t
				elif(i < j):
					A[i][j] = t
					U[i][j] = t
				elif(i == j):
					A[i][j] = 1

		for i in range(n):
			b[i] = input()

		for i in range(n):
			x[0][i] = input()

		count_overall[k] = gauss_seidel()
		spectral_radius[k] = calc_spectral_radius()
	plt.figure(1)
	plt.subplot(211)
	plt.plot( t_overall, count_overall,'g',linewidth=1.5)
	plt.plot(t_overall, count_overall, 'ro')
	plt.xlabel("X - Axis (t)")
	plt.ylabel("NUMBER OF ITERATIONS")
	plt.xlim(0, 1)
	plt.ylim(0, 51)
	plt.legend(loc='upper center',numpoints = 1)
	plt.subplot(212)
	plt.plot( t_overall, spectral_radius,'b', linewidth=1.5)
	plt.plot(t_overall, spectral_radius, 'ro')
	plt.xlabel("X - Axis (t)")
	plt.ylabel("SPECTRAL RADIUS")
	plt.xlim(0, 1)
	plt.ylim(0, 1)
	plt.show()

def print_ans(count):
	print("Answer : ")
	for i in range(n):
		print ("x" + str(i+1) + " : " ,end=" ")
		print("%10.6f" %float(x[(count)%3][i]))
	print("Total number of iterations required: " + str(count))

def calculate_max_dev(step):
	max = 0
	for i in range(n):
		val = math.fabs(x[(step)%3][i] - x[(step -1)%3][i])
		if(max < val):
			max = val
	return max

def calculate_lx(j, step):
	val = 0
	for i in range(n):
		val += L[j][i]*x[(step)%3][i]
	return val

def calculate_ux(j, step):
	val = 0
	for i in range(n):
		val += U[j][i]*x[(step-1)%3][i]
	return val

def print_aug(a):
	for i in range(n):
		for j in range(n):
			print ("%10.5f" %float(a[i][j]), end = " ")
		print()
	print()

def calc_spectral_radius():
	for i in range(n):
		L[i][i] = 1
	B = np.linalg.inv(L)
	C = np.dot(B,U)
	print("C : ")
	print_aug(C)
	e_vals = np.linalg.eigvals(C)
	spectral_rad = 0
	for i in e_vals:
		s = abs(i)
		if(spectral_rad < s):
			spectral_rad = s
	print("Spectral Radius : " + str(spectral_rad))
	print(" ========================================================= \n")
	return spectral_rad

def gauss_seidel():
	count = 0
	while True:
		count += 1
		for i in range(n):
			lx = calculate_lx(i,count)
			ux = calculate_ux(i,count)
			x[(count)%3][i] = b[i] - ux - lx
		print(str(count),end="   " )
		for i in range(n):
			print ("%10.6f" %float(x[(count)%3][i]), end = " ")
		print("\n")
		if calculate_max_dev(count) <= pow(10,-4) :
			break
	print_ans(count)
	return count

main()
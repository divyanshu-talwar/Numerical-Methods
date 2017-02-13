from __future__ import print_function
from fractions import Fraction
import numpy as np
import sympy as sp

n = input("Enter the number of equations in the system : ")
A = [[0 for j in range(4)] for i in range(n)]
y = [0 for j in range(n)]

def main():
	for i in range (n):
		print("Equation number " + str(i+1) + " : ")
		temp = raw_input()
		temp = temp.split(" ")
		for j in range(4):
			A[i][j] = Fraction(temp[j])
	calc_y(n)

def print_aug():
	for i in range(n):
		for j in range(4):
			print ("%10.5f" %float(A[i][j]), end = " ")
			# print(float(A[i][j]), end = " ")
		print()
	print()

def print_ans():
	for i in range(n):
		print ("y" + str(i+1) + " : " + str(float(y[i])))

def calc_y(t):
	print_aug()
	for i in range(1,t):
		mf = Fraction(A[i][0]/A[i-1][1]) 
		A[i][0] -= Fraction((mf)*A[i-1][1])
		A[i][1] -= Fraction((mf)*A[i-1][2])
		A[i][3] -= Fraction((mf)*A[i-1][3])
	print("Augmented matrix after thomas's algo : ")
	print_aug()

	y[t-1] = Fraction((A[t-1][3]/A[t-1][1]))

	for j in range(t-2,-1,-1):
		y[j] = Fraction((A[j][3] - A[j][2] * y[j+1])/A[j][1])

	print_ans()

main()
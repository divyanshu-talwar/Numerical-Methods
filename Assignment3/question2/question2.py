from __future__ import print_function
from fractions import Fraction
import numpy as np
import sympy as sp
import math

# n = input("Enter the number of equations in the system : ")
n = input()
A = [[0 for j in range(n+1)] for i in range(n)]
y = [0 for j in range(n)]
flag = 0

def main():
	for i in range (n):
		# print("Equation number " + str(i+1) + " : ")
		temp = raw_input()
		temp = temp.split(" ")
		for j in range(n+1):
			A[i][j] = Fraction(temp[j])
	calc_y(n)

def swap(s1, s2):
    return s2, s1

def swap_row(j,k):
	for i in range(k,n+1):
		(A[j][i], A[k][i]) = swap(A[j][i], A[k][i])

def print_aug():
	for i in range(n):
		for j in range(n+1):
			print ("%10.5f" %float(A[i][j]), end = " ")
			#print(float(A[i][j]), end = " ")
		print()
	print()

def print_ans():
	for i in range(n):
		print ("x" + str(i+1) + " : " + str(float(y[i])))

def calc_y(n):
	print_aug()
	for k in range(n-1):
		count = 0
		# count_b = 0
		pivot = k
		for j in range(k,n):
			if(A[j][k] == 0):
				count += 1
			if(A[j][n] == 0):
				count_b += 1
			if(math.fabs(A[j][k]) > math.fabs(A[pivot][k])):
				pivot = j
		if count == n-k:
			continue;
			# if count_b == n-k :
			# 	print("Infinitely many Solutions Exist !!")
			# else:
			# 	print("No Solution !!")
			# exit()
		else :
			swap_row(pivot,k)
			for j in range(k+1,n):
				mf = Fraction(A[j][k]/A[k][k])
				for t in range(k,n+1):
					A[j][t] = Fraction(Fraction(A[j][t]) - Fraction(mf* A[k][t]))
		print("Augmented Matrix after " +str(k+1)+ " Pass : \n ")
		print_aug()

	if A[n-1][n-1] == 0 and A[n-1][n] != 0 :
		print("No Solution !!")
		exit()

	if A[n-1][n-1] == 0 :
		print("Infinitely many Solutions Exist !!")
		exit()

	for i in range(n):
		count_b = 0
		for j in range(n):
			if(A[i][j] == 0):
				count += 1
		if(count == n-1):
			flag = 1
			if(A[n-1][n] != 0):
				print("No Solution !!")
				exit()

	if(flag == 1):
		print("Infinitely many Solutions Exist !!")
		exit()

	y[n-1] = Fraction(A[n-1][n]/A[n-1][n-1])
	for i in range(n-2,-1,-1):
		back_subs = 0
		for j in range(i+1,n):
			back_subs += Fraction(y[j]*A[i][j])
		y[i] = (Fraction(A[i][n] - back_subs)/A[i][i])
	print_ans()

main()
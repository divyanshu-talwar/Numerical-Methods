from __future__ import print_function
from fractions import Fraction
import numpy as np
import sympy as sp
import math

n = input()
A = [[0 for j in range(2*n)] for i in range(n)]
A_copy = [[0 for j in range(n)] for i in range(n)]
A_inv = [[0 for j in range(n)] for i in range(n)]
result = [[0 for j in range(n)] for i in range(n)]
y = [0 for j in range(n)]
H = [[0 for j in range(n)] for i in range(n)]
U = [[0 for j in range(n)] for i in range(n)]

def main():
	for i in range (n):
		temp = raw_input()
		temp = temp.split(" ")
		for j in range(n):
			A[i][j] = Fraction(temp[j])
			A_copy[i][j] = Fraction(temp[j])
		for j in range(n):
			A[i][n+j] = 1 if (i == j) else 0
	gauss_jordan()

def swap(s1, s2):
    return s2, s1

def swap_row(j,k):
	if(j != k):
		for i in range(k,2*n):
			(A[j][i], A[k][i]) = swap(A[j][i], A[k][i])

def print_aug():
	for i in range(n):
		for j in range(2*n):
			print ("%10.5f" %float(A[i][j]), end = " ")
		print()
	print()

def print_ans():
	print("Inverse of the matrix is : ")
	for i in range(n):
		for j in range(n,2*n):
			A_inv[i][j-n] = A[i][j]
			print ("%10.5f" %float(A[i][j]), end = " ")
			# print(A[i][j], end = " ")
		print()
	print()

def print_func(a):
	for i in range(n):
		for j in range(n):
			print ("%10.5f" %float(a[i][j]), end = " ")
		print()
	print()

def verify():
	print("Verification : \n \t A x A_inv : ")
	for i in range(n):
		for j in range(n):
			for k in range(n):
				result[i][j] += (A_inv[i][k] * A_copy[k][j])
	print_func(result)

def gauss_jordan():
	print("To find the Inverse of A : ")
	print_func(A)
	print("The Augmented Matrix is : ")
	print_aug()
	for k in range(n-1):
		count = 0
		pivot = k
		for j in range(k,n):
			if(A[j][k] == 0):
				count += 1
			if(math.fabs(A[j][k]) > math.fabs(A[pivot][k])):
				pivot = j
		if count == n-k:
			print("A is singular !!")
			exit()
		else :
			swap_row(pivot,k)
			for j in range(k+1,n):
				mf = Fraction(A[j][k]/A[k][k])
				for t in range(k,2*n):
					A[j][t] = Fraction(Fraction(A[j][t]) - Fraction(mf* A[k][t]))
		print("Augmented Matrix after " +str(k+1)+ " Pass : \n ")
		print_aug()

	if A[n-1][n-1] == 0 :
		print("A is singular !!")
		exit()

	print_aug()
	
	for i in range(n):
		for j in range(2*n):
			if(j<n):
				U[i][j] = A[i][j]
			else:
				H[i][j-n] = A[i][j]

	for k in range(n-1,-1,-1):
		temp = A[k][k]
		for j in range(k,2*n):
			A[k][j] = Fraction(A[k][j]/temp)
		for j in range (k-1,-1,-1):
			mf = Fraction(A[j][k])
			for t in range(k,2*n):
				A[j][t] = Fraction(Fraction(A[j][t]) - Fraction(mf * A[k][t]))
		print("Augmented Matrix after " +str(2*n-1-k)+ " Pass : \n ")
		print_aug()
	print("H : \n")
	print_func(H)
	print("U : \n")
	print_func(U)
	print_ans()
	verify()

main()
from __future__ import print_function
from fractions import Fraction
import numpy as np
import sympy as sp
import math

n = input()
A = [[0 for j in range(n)] for i in range(n)]
y = [0 for j in range(n)]
L = [[0 for j in range(n)] for i in range(n)]
B = [0 for j in range(n)]
PB = [0 for j in range(n)]
P = [j for j in range(n)]
C = [0 for j in range(n)]

def main():
	for i in range (n):
		temp = raw_input()
		temp = temp.split(" ")
		for j in range(n):
			A[i][j] = Fraction(temp[j])
	for i in range(n):
		temp = raw_input()
		B[i] = Fraction(temp)

	for i in range(n):
		L[i][i] = 1
	lu_factorisation()

def swap(s1, s2):
    return s2, s1

def swap_row(j,k):
	if(j != k):
		for i in range(k,n):
			(A[j][i], A[k][i]) = swap(A[j][i], A[k][i])
		for i in range(0,k):
			(L[j][i], L[k][i]) = swap(L[j][i], L[k][i])
		P[j],P[k] = swap(P[j],P[k])

def print_aug(a):
	for i in range(n):
		for j in range(n):
			print ("%10.5f" %float(a[i][j]), end = " ")
		print()
	print()

def print_ans(t):
	print("Answer : ")
	for i in range(n):
		print ("x" + str(i+1) + " : " + str(float(t[i])))

def print_func(a):
	for i in range(n):
		print ("%10.5f" %float(a[i]), end = " ")
	print()

def lu_factorisation():
	print("L :")
	print_aug(L)
	print("U :")
	print("P :")
	print(P)
	print_aug(A)
	for k in range(n-1):
		count = 0
		pivot = k
		for j in range(k,n):
			if(A[j][k] == 0):
				count += 1
			if(math.fabs(A[j][k]) > math.fabs(A[pivot][k])):
				pivot = j
		if count == n-k:
			print("Infinitely many Solutions Exist !!")
			exit()
		else :
			swap_row(pivot,k)
			for j in range(k+1,n):
				mf = L[j][k] = Fraction(A[j][k]/A[k][k])
				for t in range(k,n):
					A[j][t] = Fraction(Fraction(A[j][t]) - Fraction(mf* A[k][t]))
		print("Augmented Matrix after " +str(k+1)+ " Pass : \n ")
		print("L :")
		print_aug(L)
		print("U :")
		print_aug(A)
		print("P :")
		print(P)

	for i in range(n):
		PB[i] = B[P[i]]
	print("PB : ")
	print_func(PB)
	C[0] = Fraction(PB[0])
	for i in range(1,n):
		forward_subs = 0
		for j in range(0,i):
			forward_subs += Fraction(C[j]*L[i][j])
		C[i] = Fraction(PB[i] - forward_subs)
	print("C : ")
	print_func(C)

	for i in range(n):
		if A[i][i] == 0 :
			if (C[i] == 0):
				print("Infinitely many Solutions Exist !!")
				exit()
			else:
				print("No solution !!")
				exit()

	y[n-1] = Fraction(C[n-1]/A[n-1][n-1])
	for i in range(n-2,-1,-1):
		back_subs = 0
		for j in range(i+1,n):
			back_subs += Fraction(y[j]*A[i][j])
		y[i] = (Fraction(C[i] - back_subs)/A[i][i])
	print_ans(y)

main()
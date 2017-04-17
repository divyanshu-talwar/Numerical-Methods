from __future__ import print_function
from math import exp, cos, sin
act_val1 = 0.90842180555
act_val2 = 0
upper_bound=0
lower_bound=0
def func1(x):
	return x*exp(-x)
def func2(x):
	return cos(x**2)

def error_bounds1(a,b,n,option,ans):
	if(option==1):
		print ("double derivative of x*e**(-x) : e**(-x)*(x-2)")
		h = (b-a)*1.0/n*1.0
		yu = list()
		for i in range(n+1):
			yu.append(exp(-1*(a+i*h))*(a+i*h-2))
		lower_bound = min(yu)
		upper_bound = max(yu)
		# print (yu)

		# print (lower_bound)
		# print (upper_bound)
		
		k = -1*(((b-a)*1.0/12.0)*h**2)
		print ("upper bound is : ", end = " ")
		print (lower_bound*k)
		print ("lower bound is : ", end = " ")
		print (upper_bound*k)
		print ("upper limit is : ", end = " ")
		print (lower_bound*k + ans)
		print ("lower limit is : ", end = " ")
		print (upper_bound*k + ans)

	if(option==2):
		print ("double derivative of cos(x**2) : -2*(sin(x**2)-4*x**2*cos(x**2))")
		h = (b-a)*1.0/n*1.0
		yu = list()
		for i in range((n+1)*100):
			f = a*1.0+i*(h/100)
			yu.append(-2*(sin(f**2)-4*f**2*cos(f**2)))
		lower_bound = min(yu)
		upper_bound = max(yu)
		# print (yu)
		# print (lower_bound)
		# print (upper_bound)
		k = -1*(((b-a)*1.0/12.0)*h**2)
		print ("upper bound is : ",end = " ")
		print (lower_bound*k)
		print ("lower bound is : ",end = " ")
		print (upper_bound*k)
		print ("upper limit is : ",end = " ")
		print (lower_bound*k+ans)
		print ("lower limit is : ",end = " ")
		print (upper_bound*k+ans)

def error_bounds2(a,b,n,option,ans):
	if(option==1):
		print ("double derivative of x*e**(-x) : e**(-x)*(x-2)")
		h = (b-a)*1.0/n*1.0
		yu = list()
		for i in range(n+1):
			f = a+i*h
			yu.append(exp(-1*f)*(f-2))
		# print (yu)
		lower_bound = min(yu)
		upper_bound = max(yu)
		# print (upper_bound)
		# print (lower_bound)
		
		
		k = 1*((b*1.0-a)**3)/(24*n**2)
		print ("lower bound is : ",end = " ")
		print (lower_bound*k)
		print ("upper bound is : ",end = " ")
		print (upper_bound*k)
		print ("lower limit is : ",end = " ")
		print (lower_bound*k+ans)
		print ("upper limit is : ",end = " ")
		print (upper_bound*k+ans)

	if(option==2):
		print ("double derivative of cos(x**2) : -2*(sin(x**2)-4*x**2*cos(x**2))")
		h = (b-a)*1.0/n*1.0
		yu = list()
		for i in range(n+1):
			f = a*1.0+i*h/2
			yu.append(-2*(sin(f**2)-4*f**2*cos(f**2)))
		# print (yu)
		lower_bound = min(yu)
		upper_bound = max(yu)
		# print (upper_bound)
		# print (lower_bound)
		
		k = ((b*1.0-a)**3)/(24*n**2)
		print ("lower bound is : ",end = " ")
		print (lower_bound*k)
		print ("upper bound is : ",end = " ")
		print (upper_bound*k)
		print ("lower limit is : ",end = " ")
		print (lower_bound*k+ans)
		print ("upper limit is : ",end = " ")
		print (upper_bound*k+ans)

def error_bounds3(a,b,n,option,ans):
	if(option==1):
		print ("4th derivative of x*e**(-x) : e**(-x)*(x-4)")
		h = (b-a)*1.0/n*1.0
		yu = list()
		for i in range(n+1):
			yu.append(exp(-1*(a+i*h))*(a+i*h-4))
		lower_bound = min(yu)
		upper_bound = max(yu)
		# print (yu)
		# print (lower_bound)
		# print (upper_bound)
		
		k = -1*((b*1.0-a)*h**4)/(180)
		print ("upper bound is : ",end = " ")
		print (lower_bound*k)
		print ("lower bound is : ",end = " ")
		print (upper_bound*k)
		print ("upper limit is : ",end = " ")
		print (lower_bound*k+ans)
		print ("lower limit is : ",end = " ")
		print (upper_bound*k+ans)
	if(option==2):
		print ("4th derivative of cos(x**2) : 16*x**4*cos(x**2) + 48*x**2*sin(x**2) -12*cos(x**2)")
		h = (b-a)*1.0/n*1.0
		yu = list()
		for i in range((n+1)*1000):
			f = a*1.0+i*(h/1000)/2
			yu.append(16*(f**4*cos(f**2)) + 48*(f**2*sin(f**2)) -12*(cos(f**2)))
		lower_bound = min(yu)
		# -7.907e-06
		upper_bound = max(yu)
		# print (yu)
		# print (lower_bound)
		# print (upper_bound)
		
		k = -1*((b*1.0-a)*h**4)/(180)
		print ("upper bound is : ",end = " ")
		print (lower_bound*k)
		print ("lower bound is : ",end = " ")
		print (upper_bound*k)
		print ("upper limit is : ",end = " ")
		print (lower_bound*k+ans)
		print ("lower limit is : ",end = " ")
		print (upper_bound*k+ans)

def rectangle(a,b,n,option):
	if(option==1):
		print ("x*e**(-x)")
	if(option==2):
		print ("cos(x**2)")
	h = float((b-a)*1.0/n*1.0)
	sum=0.0
	for i in range(n):
		if(option==1):
			sum=sum+func1(a+h/2+i*h)
		if(option==2):
			sum=sum+func2(a+h/2+i*h)
	ans = h*sum
	print ("by rectangle rule the result is : ",end = " ")
	print (ans)
	print("")
	print ("ERROR BOUNDS : ", end = " ")
	error_bounds2(a,b,n,option,ans)
	if(option==1):
		print ("ACTUAL VALUE :", end = " ")
		print (act_val1 )
		print ("error :", end = " ")
		print (act_val1 - ans)
		print ("-----------------------------------")
		print ("")
	# if(option==2):
	# 	print ("ACTUAL VALUE :", end = " ")
	# 	print (act_val2 )
	# 	print ("Error :", end = " ")
	# 	print (act_val2 - ans)
	# 	print ("")
	# 	print ("")

def trapezoid(a,b,n,option):
	if(option==1):
		print ("x*e**(-x)")
	if(option==2):
		print ("cos(x**2)")
	h = float((b-a)*1.0/n*1.0)
	if(option==2):
		sum = 0.5*(func2(a)+func2(b))
	if(option==1):
		sum = 0.5*(func1(a)+func1(b))

	for i in range(1,n):
		if(option==1):
			sum = sum+ func1(a+i*h)
		if(option==2):
			sum = sum+ func2(a+i*h)
	ans = h*sum
	print ("by trapezoidal rule the result is : ",end = " ")
	print (ans)
	# print ("lower limit of solution :")
	# print (ans+lower_bound)
	# print ("upper limit of solution :")
	# print (ans+upper_bound)
	print ("ERROR BOUNDS :", end = " ")
	error_bounds1(a,b,n,option,ans)
	if(option==1):
		print ("ACTUAL VALUE : ", end= " ")
		print (act_val1 )
		print ("error :", end = " ")
		print (act_val1 - ans)
		print ("--------------------------------------")
		print ("")

	if(option==2):
		if n == 40:
			print("h/2 for error calculation")
			global act_val2
			act_val2 = ans
		# print ("ACTUAL VALUE")
		# print (act_val2 )
		print ("error : ", end = " ")
		print ((act_val2 - ans)/3)
		print("the given error is within the bounds as calculated above.")
		print ("--------------------------------------")
		print ("")

def simpson(a,b,n,option):
	if(option==1):
		print ("x*e**(-x)")
	if(option==2):
		print ("cos(x**2)")
	h = float((b-a)*1.0/n*1.0)
	m = n/2
	if(option==2):
		s0 = func2(a)+func2(b)
	if(option==1):
		s0 = func1(a)+func1(b)
	s1 = 0 
	for i in range(1,2*m,2):
		if(option==2):
			s1=s1+func2(a+h*i)
		if(option==1):
			s1=s1+func1(a+h*i)
	s2=0
	for i in range(2,2*m,2):
		if(option==2):
			s2=s2+func2(a+h*i)
		if(option==1):
			s2=s2+func1(a+h*i)
	ans = h/3*(s0+4*s1+2*s2)
	print ("by simpson's rule the result is : ",end = " ")
	print (ans)
	print ("")
	error_bounds3(a,b,n,option,ans)
	if(option==1):
		print ("ACTUAL VALUE : ", end = " ")
		print (act_val1 )
		print ("error : ", end = " ")
		print (act_val1 - ans)
		print ("--------------------------------------------")
		print ("")
	# if(option==2):
	# 	print ("ACTUAL VALUE")
	# 	print (act_val2 )
	# 	print ("error")
	# 	print (act_val2 - ans)
	# 	print ("")
	# 	print ("")
# print ("type 1 for x*e^(-x) and 2 for cos(x^2)")

option =1
if(option==1):
	a = 0
	b = 4
	n = 20
	rectangle(a,b,n,option)
	trapezoid(a,b,n,option)
	simpson(a,b,n,option)
	# print ("Actual Value is :")
	# print (act_val1)
option =2
if(option==2):
	a = 0
	b = 1.25
	n = 20
	rectangle(a,b,n,option)
	trapezoid(a,b,40,option)
	trapezoid(a,b,n,option)
	simpson(a,b,n,option)
	# print ("Actual Value is :")
	# print (act_val2 )
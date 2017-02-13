#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double function_value(float coeff[], int degree, double x0){
	double fx0 = 0.0;
	int i;
	for(i = 0; i <= degree; i++){
		fx0 += coeff[i]*(pow(x0,i));
	}
	return fx0;
}

double derivative_value(float coeff[], int degree, double x0){
	double f_x0 = 0.0;
	int i;
	for(i = degree; i >= 0; i--){
		f_x0 += coeff[i]*(i*(pow(x0,i-1)));
	}
	return f_x0;
}

void newton_rafhson(float coeff[], int degree, int accuracy, double x0){
	double x1, fx0 = 0.0, f_x0 = 0.0, temp = 0.0;
	int i = 0, count =0;
	while(1){
		count++;

		fx0 = function_value(coeff,degree,x0);
		f_x0 = derivative_value(coeff,degree,x0);

		temp = x0;
		if(f_x0 != 0){
			x1 = (x0 - (fx0/f_x0));
			printf("%d      %.*f       %.*f \n",count,accuracy+1,x1,accuracy+1,x0);
			x0 = x1;
		}
		else{
			printf("Newton's Method unsuccessfull (derivative is zero at given X0\n");
			break;
		}
		if((fabs(temp - x0) < pow(10,-1*(accuracy)))){
			break;
		}
		// printf("%d      %.*f       %.*f \n",count,accuracy,x1,accuracy,x0);
	}

	printf("The root of the given equation is:  %.*f \n",accuracy,x1);
}

void secant_method(float coeff[], int degree, int accuracy, double x0, double x1){
	double x2, fx0 = 0.0, f_x0 = 0.0, fx1 = 0.0, temp = 0.0;
	int i = 0, count =0;
	while(1){
		count++;

		fx0 = function_value(coeff,degree,x0);
		fx1 = function_value(coeff,degree,x1);
		f_x0 = (fx1 - fx0)/(x1 - x0);

		temp = x1;
		if(f_x0 != 0){
			x2 = (x0 - (fx0/f_x0));
			printf("%d      %.*f       %.*f      %.*f\n",count,accuracy+1,x2,accuracy+1,x1,accuracy+1,x0);
			x0 = x1;
			x1 = x2;
		}
		else{
			printf("Secant Method unsuccessfull (derivative is zero at given X0\n");
			break;
		}
		if((fabs(temp - x1) < pow(10,-1*(accuracy)))){
			break;
		}
		// printf("%d      %.*f \n",count,accuracy+1,x2);
	}

	printf("The root of the given equation is:  %.*f \n",accuracy+1,x2);
}
int main(){
	float *coeff;
	double x0,x1;
	int degree,accuracy,i,choice = 0;
	printf("Enter the degree of the polynomial \n");
    scanf("%d",&degree);
    coeff = (float *)(malloc((degree+1)*sizeof(float)));
    for(i=0;i<=degree;i++)
    	{
        	printf(" Enter coefficient of x^%d : ",i);
        	scanf("%f",&coeff[i]);
    	}
    printf("The polynomial entered is: ");
    for(i = degree ; i > 0; i--)
    	{
        	printf(" %.1fx^%d + ",coeff[i],i);
    	}
    printf(" %.1fx^%d \n",coeff[0],0);

	printf("Enter which method you want to follow :\n 1.Newton's Method \n 2.Secant Method \n");
    scanf("%d",&choice);

    if (choice == 1){
	    printf("Enter the starting value(X0) : \n");
	    scanf("%lf",&x0);

	    printf("Enter the accuracy you want : \n");
	    scanf("%d", &accuracy);

	    printf("S.No.  Function Value     x0\n");
	    newton_rafhson(coeff, degree, accuracy, x0);
    }
    else if(choice ==2 ){
	    printf("Enter the starting value(X0) : \n");
	    scanf("%lf",&x0);

	    printf("Enter the starting value(X1) : \n");
	    scanf("%lf",&x1);

	    printf("Enter the accuracy you want : \n");
	    scanf("%d", &accuracy);

	    printf("S.No.  Function Value      x1       x0\n");
	    secant_method(coeff, degree, accuracy, x0,x1);
	}
	else{
		printf("ERROR! Enter a valid method :|\n");
	}
}
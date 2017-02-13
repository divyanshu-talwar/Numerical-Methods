#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int flag =0;
void fixed_point_iteration(int accuracy, double x0){
	double x1 = 0.0, temp = 0.0;
	int i = 0, count =0;
	do{
		count++;

		x1 = pow(x0,4) + 0.2;
		if(x0 ==1){
			flag = 1;
		}
		if(flag){
			x1 = pow((x0 - 0.2), 0.25);

		}
		printf("%d      %.*f           %.*f \n",count,accuracy+1,x1,accuracy+1,x0);
		temp = x0;
		x0 = x1;
	}while((fabs(temp - x0) >= pow(10,-1*(accuracy))));

	printf("The root of the given equation is:  %.*f \n",accuracy,x1);
}

int main(){
	float *coeff;
	double x0;
	int degree,accuracy,i;
	// printf("Enter the degree of the polynomial \n");
 //    scanf("%d",&degree);
 //    coeff = (float *)(malloc((degree+1)*sizeof(float)));
 //    for(i=0;i<=degree;i++)
 //    	{
 //        	printf(" Enter coefficient of x^%d : ",i);
 //        	scanf("%f",&coeff[i]);
 //    	}
 //    printf("The polynomial entered is: ");
 //    for(i = degree ; i > 0; i--)
 //    	{
 //        	printf(" %.1fx^%d + ",coeff[i],i);
 //    	}
 //    printf(" %.1fx^%d \n",coeff[0],0);

    printf("Enter the starting value(X0) : \n");
    scanf("%lf",&x0);

    printf("Enter the accuracy you want : \n");
    scanf("%d", &accuracy);

    printf("S.No.  Function Value   x0\n");
    fixed_point_iteration(accuracy,x0);
}
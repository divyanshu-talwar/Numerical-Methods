#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void newton_rafhson(float coeff, int degree, int accuracy, double x0){
	double x1, fx0 = 0.0, f_x0 = 0.0, temp = 0.0;
	int i = 0, count =0;
	while(1){
		count++;

		fx0 = pow(x0,degree) - coeff;
		f_x0 = degree*pow(x0,degree-1);

		temp = x0;
		if(f_x0 != 0){
			x1 = (x0 - (fx0/f_x0));
			x0 = x1;
		}
		else{
			printf("Newton's Method unsuccessfull (derivative is zero at given X0\n");
			break;
		}
		if((fabs(temp - x0) < pow(10,-1*(accuracy)))){
			break;
		}
		printf("%d      %.*f \n",count,accuracy,x1);
		// printf("%lf %lf \n",fabs(temp - x0), pow(10,-1*(accuracy)) );
	}

	printf("The value of %d th root of %f is :  %.*f \n",degree, coeff, accuracy,x1);
}

int main(){
	float coeff;
	double x0,x1;
	int degree,accuracy,i;
	printf("Enter the value of k : \n");
    scanf("%d",&degree);

	printf("Enter the value of c : \n");
    scanf("%f",&coeff);

    if(coeff < 0 && degree % 2 == 0){
    	printf("ERROR! c can't be negative \n");
    	exit(0);
    }
    printf("Enter the starting value(X0) : \n");
    scanf("%lf",&x0);

    printf("Enter the accuracy you want : \n");
    scanf("%d", &accuracy);

    printf("S.No.  x0\n");
    newton_rafhson(coeff, degree, accuracy, x0);
}
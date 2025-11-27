#include <stdio.h>
#include <math.h>

int main()
{double x;
printf("Enter the value of x\n");

scanf("%lf", &x);

printf("the end result is:%f\n", pow(x,3.0)+ 3*pow(x,2.0)+5*x+7);

    return 0;
}

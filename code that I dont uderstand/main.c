#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main()
{

    double x;
double result;


printf("Enter a value for x:");
scanf("%lf",&x);

result=pow(x,3.0)+3*pow(x,2.0)+5*x+7;
printf("x*x*x+3*x*x+5*x+7=%f\n", result);

}

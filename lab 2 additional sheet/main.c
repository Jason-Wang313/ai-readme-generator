#include <stdio.h>
#include <math.h>
#define PI  3.14

int main()
{double  v;
double r;
printf("Enter the volume of the sphere:\n");
scanf("%lf", &v);
r = pow((3*v)/(4*PI), 1.0 / 3.0);
printf("The value of r is:%f\n", r);


    return 0;
}

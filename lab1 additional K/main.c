#include <stdio.h>
#include <math.h>
int main()
{double a, b;
double x1, x2, x3, x4;
printf("Enter a and b");
scanf("%lf %lf", &a, &b);

x1=sin(a+b);
x2=sin(a)*cos(b)+cos(a)*sin(b);

if(fabs(cos(a))<1e-5)
    {printf("Error:cos(a) is too close to zero, can't calculate tan(a)\n");}
    else{x3= tan(a);
    x4=sin(a)/cos(a);
    printf("here are the values for x3 and x4:%f %f\n", x3,x4);}


return 0;
}

#include <stdio.h>
#include <math.h>

int main()
{double a, b, c,x1,x2;
printf("Enter a, b ,c\n");
scanf("%lf %lf %lf", &a, &b, &c);
x1=(-b+sqrt(b*b-4*a*c))/(2*a);
x2=(-b-sqrt(b*b-4*a*c))/(2*a);
printf("x1 is %f\n",x1);
printf("x2 is %f\n",x2);



    return 0;
}

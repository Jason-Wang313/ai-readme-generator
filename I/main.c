#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main()
{  double a;
   double b;
   double c;
   double x1;
   double x2;
  printf("Enter a, b, and c : ");//Ask the user for input
  scanf("%lf %lf %lf", &a, &b, &c); //read the three doubles from the user;
  x1 = (-b+sqrt(b*b-4*a*c))/(2*a); //calculate the first root
  x2 = (-b-sqrt(b*b-4*a*c))/(2*a); // calculate the first root
  printf("The solutions are: %f and %f\n", x1, x2);//To print doubles with printf, you use the %f format specifier
    return 0;
}

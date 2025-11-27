#include <stdio.h>
#include <math.h>

int main()
{int a,b;
float c ;
printf("Enter the value of a and b:\n");
scanf("%d%d", &a, &b);
c=  (float)a/ (float)b;
printf("The value of c is: %f", c);
scanf("%f", &c);
    return 0;
}

#include <stdio.h>
#include <stdlib.h>
#include <stdio.h>

int main(void)
{
    int a,b,c,product;

    printf("Enter a and b and c:");
    scanf("%d%d%d",&a,&b,&c);

    product=a*b*c;

    printf("%d * %d * %d = %d\n",a,b,c,product);

    return 0;
}

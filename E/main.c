#include <stdio.h>
#include <stdlib.h>

int main()
{
   int w=32;
   int x=8;
   int y=10;
   int z;
   z=2*y*(w+x);
    printf("2*%d*(%d+%d)=%d\n", y, w, x, z);
    return 0;
}

#include <stdio.h>
#include <stdlib.h>


int main(){int n;//user input
int i;//loop counter
float factorial = 1.0;//result. must start at 1.0
 printf("Enter a number (max 20):\n");
scanf("%d", &n);
// loop from 1 up to n
for (i=1; i<=n; i++) {
    //Multiply current factorial by the counter 'i'
    factorial = factorial *i;

}


//print the result(using the %.0f to show it as a whole number)
printf("Factorial of %d is %.0f\n", n, fatorial)




    return 0;
}

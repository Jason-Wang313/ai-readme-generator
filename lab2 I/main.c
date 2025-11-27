#include <stdio.h>
#include <stdlib.h>

int main()
{
    int sum = 0;
    int i // loop counter
    int num // user input variable
    printf("Enter 6 numbers :\n");
    // 6 times loops
    for(i=1; i<=6; i++ ){
        printf("Enter number %d:", i);
        scanf("%d", &num) // store the number
        sum= sum + num;  // calculate new result and save it back to the old value of sum
        printf("the final sum is: %d\n", sum); // display the final sum


    }





    return 0;
}

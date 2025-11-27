#include <stdio.h>

int main() {
    printf("The surviving numbers are:\n");

    // 1. Loop from 1 to 150
    for (int i = 1; i <= 150; i++) {

        // 2. The Logic Filter
        // Complete this line to check 5, 7, 11, and 13 as well!
        if (i % 2 != 0 && i % 3 != 0 &&i % 5 != 0 && i % 7 != 0 && i % 11 != 0 &&i % 13 != 0     ) {

            printf("%d ", i);
        }
    }

    printf("\n");
    return 0;
}

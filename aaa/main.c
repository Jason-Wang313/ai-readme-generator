#include <stdio.h>

int main() {
    int n;
    int i;
    float factorial = 1.0; // Initialize to 1.0

    printf("Enter the number:\n");
    scanf("%d", &n); // Don't forget the &!

    // The Logic (Perfect!)
    for (i = 1; i <= n; i++) {
        factorial = factorial * i;
    }

    // Print result with %.0f to hide decimal places
    printf("Factorial of %d is %.0f\n", n, factorial);

    return 0;
}

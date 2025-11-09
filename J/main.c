#include <stdio.h>
#include <math.h>

int main()
{
    //all variables should be doubles for math funcrion
    double x;
    double nat_log, nat_log_reverse;
    double log_10, log_10_reverse;
    // 1. Enter a value of x
    printf("Enter a value for x: ");
    scanf("%lf", &x);
    //2. Natural Logarithm
    nat_log = log (x);
    nat_log_reverse = exp(nat_log);

    printf("\n--- Natural Log (ln) ---\n");// \n adds space before and after the text
    printf("ln(%.2f) = %.5f\n", x, nat_log);  // print to 5 decimal places
    printf("e^(%.5f) = %.2f\n", nat_log, nat_log_reverse);// Print result







    return 0;
}

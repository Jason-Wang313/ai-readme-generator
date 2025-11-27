//Integral Calculator

#include <stdio.h>
#include <math.h>

int main(void) {

// Main program loop
int repeat = 0;
do {
    // --- Get Equation Order ---
    int order;
    do {
        printf("Enter order of equation (0 to 3): ");
        scanf("%d", &order);

        if (order < 0 || order > 3)
            printf("Invalid order! Please enter a value between 0 and 3.\n");
    } while (order < 0 || order > 3);

    // --- Get Coefficients ---
    double a= 0.0;
    double b =0.0;
    double c = 0.0;
    double d= 0.0;
    int confirmed = 0;

    do {
        // Reset coefficients
        a = 0.0; b = 0.0; c = 0.0; d = 0.0;

        if (order == 3) {
            printf("Enter coefficient of x^3: ");
            scanf("%lf", &d);
            printf("Enter coefficient of x^2: ");
            scanf("%lf", &c);
            printf("Enter coefficient of x^1: ");
            scanf("%lf", &b);
            printf("Enter constant term: ");
            scanf("%lf", &a);
        } else if (order == 2) {
            printf("Enter coefficient of x^2: ");
            scanf("%lf", &c);
            printf("Enter coefficient of x^1: ");
            scanf("%lf", &b);
            printf("Enter constant term: ");
            scanf("%lf", &a);
        } else if (order == 1) {
            printf("Enter coefficient of x^1: ");
            scanf("%lf", &b);
            printf("Enter constant term: ");
            scanf("%lf", &a);
        } else {
            printf("Enter constant term: ");
            scanf("%lf", &a);
        }

        // Confirm
        printf("\nConfirming that your equation is:\n");
        printf("f(x) = %.2fx^3 + %.2fx^2 + %.2fx + %.2f ?\n", d, c, b, a);
        printf("(1 for yes, 0 for no): ");
        scanf("%d", &confirmed);

        if (confirmed != 1)
            printf("Let's re-enter the coefficients.\n");

    } while (confirmed != 1);


    // --- Get Integration Limits ---
    double x1, x2;
    do {
        printf("Enter lower limit of integration (x1): ");
        scanf("%lf", &x1);
        printf("Enter upper limit of integration (x2): ");
        scanf("%lf", &x2);

        if (x1 >= x2) {
            printf("Invalid limits! Lower limit must be less than upper limit.\n");
        }
    } while (x1 >= x2);

    // --- Calculate Integral ---
    // F(x) = (d/4)x^4 + (c/3)x^3 + (b/2)x^2 + ax
    // Result = F(x2) - F(x1)

    double t4up = (d / 4.0) * pow(x2, 4);
    double t3up = (c / 3.0) * pow(x2, 3);
    double t2up = (b / 2.0) * pow(x2, 2);
    double t1up = a * x2;
    double val_x2 = t4up + t3up + t2up + t1up;

    double t4low = (d / 4.0) * pow(x1, 4);
    double t3low = (c / 3.0) * pow(x1, 3);
    double t2low = (b / 2.0) * pow(x1, 2);
    double t1low = a * x1;
    double val_x1 = t4low + t3low + t2low + t1low;

    double final_val = val_x2 - val_x1;

    // --- Display Result ---
    printf("\nThe definite integral of f(x) from x = %.2f to x = %.2f is: %.4f\n", x1, x2, final_val);

    // --- Repeat? ---
    printf("\nDo you want to enter another function? (1 for yes, 0 for no): ");
    scanf("%d", &repeat);

} while (repeat == 1);

    printf("Program finished. Goodbye!\n");
    return 0;
}

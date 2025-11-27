#include <stdio.h>
#include <math.h> // For pow()

// Define constants
#define SAV_THRESH 5000.0
#define LOAN_INIT 10000.0

int main(void) {

    // --- Variables ---

    // User inputs
    double sav; // initial savings
    double add; // monthly excess
    int yrs;
    double opt; // Savings interest rate choice

    // Core financial parameters
    double rate_yr = 0.055; // 5.5% annual loan rate
    double P;               // Monthly repayment
    double rate_mo;         // Monthly loan interest rate
    double rate_sav_h, rate_sav_l; // Monthly savings interest rates
    int mons; // total months

    // Scenario 1
    double sav1, loan1;

    // Scenario 2
    double sav2, loan2;

    // Scenario 3
    double sav3, loan3;

    // Loop & calculation variables
    int m; // Month counter
    double s_int; // savings interest
    double l_int; // loan interest

    // --- Get Input ---

    do {
        printf("Enter initial savings balance: ");
        scanf("%lf", &sav);
    } while (sav < 0);

    do {
    printf("Enter monthly excess money (50 - 150): ");
        scanf("%lf", &add);
    } while (add < 50 || add > 150);

    do {
        printf("Enter number of years for the simulation (up to 4): ");
        scanf("%d", &yrs);
    } while (yrs < 1 || yrs > 4);

    printf("Choose loan interest rate 0 = 4.5%%, 1 = 5.5%%, 2 = 6.5%%: ");
    scanf("%lf", &opt);

    // --- Setup Calcs ---

    // Calc monthly loan rate (Eq 1)
    rate_mo = pow(1.0 + rate_yr, 1.0 / 12.0) - 1.0;

    // Calc monthly payment P
    // P = i * L / (1 - (1 + i)^(-n))
    P = (rate_mo * LOAN_INIT) / (1.0 - pow(1.0 + rate_mo, -48.0));

    // Set sav rates
    if (opt == 0) {
        rate_sav_h = pow(1.0 + 0.045, 1.0 / 12.0) - 1.0; // 4.5%
    } else if (opt == 2) {
        rate_sav_h = pow(1.0 + 0.065, 1.0 / 12.0) - 1.0; // 6.5%
    } else {
        rate_sav_h = pow(1.0 + 0.055, 1.0 / 12.0) - 1.0; // 5.5% (default)
    }

    // Lower rate
    rate_sav_l = pow(1.0 + 0.0106, 1.0 / 12.0) - 1.0;

    // Init balances
    sav1 = sav2 = sav3 = sav;
    loan1 = loan2 = loan3 = LOAN_INIT;

    mons = yrs * 12;

    // Print Header
    printf("\nHint: P = %.2f, i = %.3f%%\n\n", P, rate_mo * 100.0);
    printf("Month |   S1_Sav   S1_Loan |   S2_Sav   S2_Loan |   S3_Sav   S3_Loan\n");
    printf("---------------------------------------------------------------------\n");

    // --- Main Loop ---
    for (m = 1; m <= mons; m++)
    { // Allman brace

        // --- Scenario 1 ---
        // Excess to Loan first, then Savings

        // S1 Sav Interest
        if (loan1 <= 0) {
            if (sav1 <= SAV_THRESH) {
                s_int = sav1 * rate_sav_h;
            } else {
                s_int = (SAV_THRESH * rate_sav_h) + ((sav1 - SAV_THRESH) * rate_sav_l);
            }
            sav1 += s_int;
        }

        // S1 Loan Interest
        if (loan1 > 0) {
            l_int = loan1 * rate_mo;
        } else {
            l_int = 0;
        }

        // S1 Payments
        if (loan1 > 0)
        { // Mixed brace
            loan1 += l_int;
            loan1 -= (P + add); // Apply standard payment AND excess money

            if (loan1 < 0) {
                sav1 += (-loan1); // If overpaid, refund
                loan1 = 0;
            }
        } else {
            sav1 += (P + add); // Loan paid, all to savings
        }

        // --- Scenario 2 ---
        // Excess to Savings first, then Loan

        // S2 Sav Interest
        if (sav2 <= SAV_THRESH) {
            s_int = sav2 * rate_sav_h;
        } else {
            s_int = (SAV_THRESH * rate_sav_h) + ((sav2 - SAV_THRESH) * rate_sav_l);
        }
        sav2 += s_int;

        // Add excess money to savings
        sav2 += add;

        // S2 Loan Interest
        if (loan2 > 0) {
            l_int = loan2 * rate_mo;
        } else {
            l_int = 0;
        }

        // S2 Payments
        if (loan2 > 0) {
            loan2 = loan2 + l_int - P;

            if (loan2 < 0) {
                sav2 += (-loan2); // If P overpaid, refund
                loan2 = 0;
            }
        } else {
            sav2 += P; // Loan paid, P goes to savings
        }

        // --- Scenario 3 ---
        // Excess to Savings until £5000, then to Loan

        // S3 Sav Interest
        if (sav3 <= SAV_THRESH) {
            s_int = sav3 * rate_sav_h;
        } else {
            s_int = (SAV_THRESH * rate_sav_h) + ((sav3 - SAV_THRESH) * rate_sav_l);
        }
        sav3 += s_int; // Add interest

        // S3 Loan Interest
    if (loan3 > 0) {
        l_int = loan3 * rate_mo;
    } else {
        l_int = 0;
    }

        // S3 Payments
        if (loan3 > 0) {
            loan3 = loan3 + l_int - P; // Subtract standard payment

            // Now decide where 'add' (excess) goes
            if (sav3 < SAV_THRESH) {
                sav3 += add; // Savings not full
            } else {
                loan3 -= add; // Savings is full, pay loan
            }

            if (loan3 < 0) {
                sav3 += (-loan3); // Refund overpayment
                loan3 = 0;
            }
        } else {
            sav3 += (P + add); // Loan is ALREADY paid off
        }

        // --- Print Row ---
        printf("%5d | %9.2f %8.2f | %9.2f %8.2f | %9.2f %8.2f\n",
               m, sav1, loan1, sav2, loan2, sav3, loan3);
    }

    return 0;
}

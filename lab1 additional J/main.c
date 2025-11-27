#include <stdio.h>
#include <math.h>

int main()
{
    double nat_log; double nat_log_reversed;double x;
    printf("Enter a value x\n");
    scanf("%lf",&x);
    nat_log=log(x);
    nat_log_reversed=exp(nat_log);
    printf("value of natural log:%5f\n", nat_log);
    printf("reversed value:%5f\n", nat_log_reversed);

    double log10_result,log10_reversed;
    log10_result=log10(x);//not understand
    log10_reversed=pow(10,log10_result);//not understand
    printf("log10result: %.5f\n", log10_result);
    printf("log10_reversed: %.5f\n", log10_reversed);

    return 0;
}

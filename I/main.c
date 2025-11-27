#include <stdio.h>

int main() {
   int start_hours, start_minutes, end_hours, end_minutes;
   int start_total, end_total;
   int duration_minutes;
   int hours, minutes;
   //declare variables
   printf("Enter the start (HH MM) and end(HH MM) time:\n");
   scanf("%d%d%d%d", &start_hours, &start_minutes, &end_hours, &end_minutes);//problem

   start_total = start_hours*60 + start_minutes;
   end_total = end_hours*60 + end_minutes;

   duration_minutes= end_total - start_total;

   hours = duration_minutes/60; //problem
   minutes = duration_minutes%60; //problem

   printf("The duration is %d minutes which is %d h %d m",duration_minutes, hours, minutes );




   return 0;
}

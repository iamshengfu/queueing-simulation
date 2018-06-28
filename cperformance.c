#include <stdio.h>
#include <time.h>
void main(){
    double a,t,b;
    long y;
    double x;
    time_t start,end;
    start=clock();
    for(y=0;y<1000;y++){
        for(x=0;x<10000;x++){
            a+= x*1000.000000/888/500;
        }
    }
    end = clock();
    t=(double)(end - start) / CLOCKS_PER_SEC;
    printf("time:");
    printf("%f \n",t);
    printf("a equals to ");
    printf("%.2f \n",a);
    printf("%d,%d,%d",start,end,CLOCKS_PER_SEC);
    return;
}
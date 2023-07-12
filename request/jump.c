#include <stdio.h>
#include <math.h>

int min(int a, int b){
    if (b>a)
        return a;
    else
    return b;

}

int jump_search (int arr[], int x, int n)
{
    //finding the block to be jumped
    int step = sqrt(n);
    int prev = 0;

    while (arr[min(step, n)-1] < x) 
    {
        prev = step;
        step += sqrt(n);
        if (prev >= n)
            return -1;
    }

    while (arr[prev] < x ){
        prev++
        if (prev == min(step, n))
    }

}
#include <stdio.h>

int search(int arr[], int x, int y) {
    for (int i = 0; i < y; i++)
        if (arr[i] == x) 
            return i;
    return -1;
}
int main(void){
    int arr[] = {2, 3, 4, 5, 20, 3, 15, 20 };
    int y = 20;
    int x = sizeof(arr) / sizeof(arr[0]);

    int result = search(arr, x, y);
    (result == -1 )
        ? printf("element not found in array")
        : printf("element is at index %d", result);
    return 0;
}
#include <stdio.h>
int main() {
    int num = 5, fact = 1;
    for(int i = 1; i <= num; i++) {
        fact *= i;
    }
    printf("Factorial: %d\n", fact);
    return 0;
}

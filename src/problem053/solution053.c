#include <stdio.h>

double fact(int n) {
    double ans = 1;
    int i;
    for (i = 1; i <= n; i++) {
        ans *= i;
    }
    return ans;
}

double choose(int n, int r) {
    return fact(n) / (fact(r) * fact(n - r));
}

int main() {
    int count = 0, n, k;
    for (n = 0; n <= 100; n++) {
        for (k = 0; k <= n; k++) {
            if (choose(n, k) >= 1000000) {
                count += 1;
            }
        }
    }
    printf("%d\n", count);
}

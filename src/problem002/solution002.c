#include <stdio.h>

main() {
    int total = 0, n = 1, m = 2;
    while (n < 4000000) {
        if (n % 2 == 0)
            total += n;
        int tmp = n;
        n = m;
        m = tmp + m;
    }
    printf("%d\n", total);
}
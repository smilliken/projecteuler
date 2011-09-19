#include <stdio.h>

long long solve(){
    long long n = 600851475143LL, p = 1;
    while (n > 1 && ++p)
        while (n % p == 0)
            n /= p;
    return p;
}

main(){
    printf("%lld\n", solve());
}
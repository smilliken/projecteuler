#include <stdio.h>

solve(){
    int total = 0, i;
    for (i = 0; i < 1000; ++i)
        if (i % 3 == 0 || i % 5 == 0)
            total += i;
    return total;	
}

main(){
    printf("%d\n", solve());
}
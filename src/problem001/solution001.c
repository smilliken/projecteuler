#include <stdio.h>

main()
{
    int total = 0, i;
    for (i = 0; i < 1000; ++i)
        if (i % 3 == 0 || i % 5 == 0)
            total += i;
    printf("%d\n", total);
}

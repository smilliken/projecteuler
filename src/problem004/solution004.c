#include <stdio.h>
#include <math.h>

isPalindrome(int n)
{
  int rev = 0, mod = n;
  while(mod){
    rev = 10 * rev + (mod % 10);
    mod /= 10;
  }
  return rev == n;
}

solve(){
    int n = 999, i, j;
    for(i=0;i<2*n+1;++i){
        for(j=0;j<i+1;j++){
            if((j + i) % 2 == 0){
                int a = (int)(n - (i - j - 1)/2.0);
                int pal = a * (a - j);
                if(isPalindrome(pal))
                    return pal;
            }
        }
    }
}

main(){
    printf("%d\n", solve());
}
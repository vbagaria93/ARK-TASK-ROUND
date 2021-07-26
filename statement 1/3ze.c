#include <stdio.h>
#include <string.h>
#include <stdlib.h>
int G ( int n )
   {
      if (n == 0) return 3;
      if (n == 1) return 8;
      return 5*((G(n-1)-3)/5+(G(n-2)-3)/5)+3 ;
   }
int main()
{
	printf("%d",G(7));
}
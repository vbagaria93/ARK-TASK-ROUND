#include <stdio.h>
int find_power(int a)

{

int p=1;



for (int i = 1; ;  i ++){

p=p*3;

if (p>a){

return  i -1;

}

}

}
int main()
{
    int a;
    scanf("%d",&a);
    printf("%d",find_power(a));
}

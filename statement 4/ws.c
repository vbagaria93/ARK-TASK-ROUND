 #include <stdio.h>
 
 int main ( )
   {
       char *s1 = "463 897", *p;
       *p=*s1;
       for (int i=0;i<3;i++)
       {
	  *p[i]=s1[i];
       }
       *p = '\0' ;
       printf ("%s", s1);
   }
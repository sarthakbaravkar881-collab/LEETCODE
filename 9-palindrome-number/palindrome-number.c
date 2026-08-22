bool isPalindrome(int x) {
   int n=x;
   long rev=0;
   int rem;
    if (n<0)
        return false;
    
    else{
        while (x!=0){
            rem=x%10;
            rev=(rev*10)+rem;
            x/=10;
   } 
   return n==rev;}
}
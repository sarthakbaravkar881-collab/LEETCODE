class Solution {
    public boolean isPalindrome(int x) {
        int n=x;
        double rev=0;
        int rem;
        if(x<0){
            return false;
        }
        else{
        while(x!=0){
        rem=x%10;
        rev=(rev*10)+rem;
        x/=10;
        }
        return n==rev;}
}}
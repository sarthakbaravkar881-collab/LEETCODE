class Solution {
    public int countPrimes(int n) {
        if(n<=2){
            return 0;
        }
        int count=0;
        boolean[] arr=new boolean[n];
        arr[0]=true;
        arr[1]=true;
        int limit=(int)Math.sqrt(n);
        int i,j;
        for (i=2;i<=limit;i++){
            if(arr[i]==false){
                for(j=i*i;j<n;j+=i){
                    arr[j]=true;
                }
            }
        }
        for(int a=0;a<n;a++){
            if(arr[a]==false){
                count++;
            }
        }
        return count;
    }
}
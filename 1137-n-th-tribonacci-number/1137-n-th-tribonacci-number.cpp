class Solution {
public:
    int tribonacci(int n) {
        if(n==0)return n;
        if(n==2||n==1)return 1;
        
        int a[n+2];
        a[1]=a[2]=1;
       a[0]=0;
        
        for(int i=3;i<n+1;i++){a[i]=a[i-1]+a[i-2]+a[i-3];
                            }
        
        return a[n];
    }
};
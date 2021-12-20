class Solution {
public:
    int fib(int n) {
         if (n < 2) return n;        
        
        vector<int> tmp(n+1, 0);
        tmp[0] = 0;
        tmp[1] = 1;
        tmp[2] = 2;
        
        for (int i = 3; i < n; i++) {
            tmp[i] = tmp[i-1] + tmp[i-2];
        }
        
        return tmp[n-1];}
};
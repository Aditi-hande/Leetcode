class Solution {
public:
    int climbStairs(int n) {
        
        if(n==0)return 0;
        if(n==1)return 1;
        if(n==2)return 2;
        if(n==3)return 3;
        
        vector<int>ans;
        ans.push_back(0);
        ans.push_back(1);
        ans.push_back(2);
        ans.push_back(3);
        
        for(int i=4;i<=n;i++){
            int temp=ans[i-1]+ans[i-2];
            ans.push_back(temp);
            
        }
        
        return ans[n];
        
        
    }
};
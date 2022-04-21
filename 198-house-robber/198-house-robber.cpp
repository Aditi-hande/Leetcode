class Solution {

    //note that this is top down which is essentially creating a tree but with memoisation/caching
        
        int help(vector<int>& num,int n,vector<int>&dp){
        if(n<0)return 0;
        if(dp[n]!=-1)return dp[n];
        int n1= num[n]+help(num,n-2,dp);
        int n2=help(num,n-1,dp);
        return dp[n]=max(n1,n2);
        
    }
public:
    int rob(vector<int>& nums) {
        vector<int>dp(nums.size()+1,-1);
        return help(nums,nums.size()-1,dp);
    }
};
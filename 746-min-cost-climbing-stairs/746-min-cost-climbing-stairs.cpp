class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        
        vector<int> ans;
        //ans.push_back(0);
        ans.push_back(cost[0]);
        ans.push_back(cost[1]);
        int n=cost.size();
        
        for(int i=2;i<n;i++){
            int temp=cost[i]+ min(ans[i-1],ans[i-2]);
            ans.push_back(temp);
        }
        
        return min(ans[n-1],ans[n-2]);
    }
};
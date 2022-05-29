class Solution {
public:
    vector<vector<int>>ans;
    
    void helper(vector<int>& nums,vector<int>currans,int curridx){
        
        ans.push_back(currans);
        
        for(int i=curridx;i<nums.size();i++){
            if(i>curridx && nums[i]==nums[i-1])continue;
            currans.push_back(nums[i]);
            helper(nums,currans,i+1);
            currans.pop_back();
        }
    }
    
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        
        vector<int>curans;
        sort(nums.begin(),nums.end());
        helper(nums,curans,0);
        
        return ans;
        
    }
};
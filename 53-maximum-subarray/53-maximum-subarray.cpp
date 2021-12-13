class Solution {
public:
    int maxSubArray(vector<int>& nums) {
       int cm=nums[0];
        int cmf=nums[0];
        for(int i=1;i<nums.size();i++){
           cm=max(nums[i],cm+nums[i]);
            cmf=max(cm,cmf);
        }
        return cmf; }
    
   
};
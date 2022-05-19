class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int count=0;
        int l=0;
        int h=1;
        
        while(h<nums.size()){
            if(nums[l]==nums[h]){count++;nums[h]=101;h++;}
            else{ l=h;h++;
                    }
        }
        
        sort(nums.begin(),nums.end());
        
    return nums.size()-count;}
};
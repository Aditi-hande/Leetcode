class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int high,low,mid;
        high=nums.size()-1;
        low=0;
        
        while(low<=high){
            mid=low+(high-low)/2;
            if(nums[mid]==target){return mid;}
            
            if(nums[mid]>target){ high=mid-1; }
            if(nums[mid]<target){ low=mid+1; }
            
            
        }
    return (low);}
};


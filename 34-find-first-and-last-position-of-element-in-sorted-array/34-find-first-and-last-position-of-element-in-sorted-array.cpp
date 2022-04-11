class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        //finding the first Occurence
        int first = firstOcc(nums,target);
        
        //finding the Second Occurence
        int second = SecondOcc(nums,target);
        
        return {first,second};
    }
    int firstOcc(vector<int> nums, int target){
        int n = nums.size();
        int l = 0, h = n-1;
        int res = -1;
        while( l <= h){
            int mid = (l+h)/2;
            
            if( nums[mid] < target)
                l = mid+1;
            else if( nums[mid] > target)
                h = mid-1;
            else{
                //store the current and move backward to find the first occurence  
                res= mid;
                h = mid-1;
            }
        }
        return res;
    }
    
    int SecondOcc(vector<int> nums, int target){
        int n = nums.size();
        int l = 0, h = n-1;
        int res = -1;
        while( l <= h){
            int mid = (l+h)/2;
            
            if( nums[mid] < target)
                l = mid+1;
            else if( nums[mid] > target)
                h = mid-1;
            else{
                //store the current and move forward to find the last occurence  
                res= mid;
                l = mid+1;
            }
        }
        return res;
    }
    
};
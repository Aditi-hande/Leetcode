class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int size = nums.size(), i = 0, j = 1;
    
		if(size == 0)
			return 0;  //Exclude edge case
    
		for(j = 1; j<size; j++)
		{
			//If the numbers are same, do nothing, if different, copy the different new number next to the initial number
			if(nums[i]!=nums[j])
			{
				i+=1;
				nums[i] = nums[j];
			}
		}
        
        //for(auto ele:nums){cout<<ele<<" ";}
    
		return i+1;}
};
class Solution {
public:
    int rob(vector<int>& nums) {
        
        if(nums.size()==1)return nums[0];
        if(nums.size()==2)return (max(nums[0],nums[1]));
        
        
        int mx1=0,mx2=0;
        for(int i=0;i<nums.size()-1;i++){
            int temp=mx2;
            mx2=max(mx2,mx1+nums[i]);
            mx1=temp;
            //cout<<mx1<<mx2<<" ";
        }
        
        int m1=0,m2=0;
        for(int i=1;i<nums.size();i++){
            int temp1=m2;
            m2=max(m2,m1+nums[i]);
            m1=temp1;
            //cout<<mx1<<mx2<<" ";
        }
        
        return(max(m2,mx2));
    }
};
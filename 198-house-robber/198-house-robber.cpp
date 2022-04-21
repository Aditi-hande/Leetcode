class Solution {
public:
    int rob(vector<int>& nums) {
        
        //note that this is bottom up as we are tabulating results and then giving final ans
        
        int mx1=0,mx2=0;
        for(int i=0;i<nums.size();i++){
            int temp=mx2;
            mx2=max(mx2,mx1+nums[i]);
            mx1=temp;
            cout<<mx1<<mx2<<" ";
        }
        return mx2;}
};
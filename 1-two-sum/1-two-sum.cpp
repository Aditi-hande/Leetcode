class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector <int> ans;
        int ele;
        auto j=0;
        unordered_map<int,int> map;
       unordered_map<int,int>:: iterator k;
        //sort(nums.begin(),nums.end());
        for (int i=0;i<nums.size(); i++){
            
            map.insert(make_pair(nums[i],i));
               
            }
        for (int i=0;i<nums.size(); i++){
            
                 ele=target-nums[i];
            k=map.find(ele);
                if(k!=map.end() && k->second!=i){ ans.push_back(i); 
                                 ans.push_back(k->second);
                                break;}
            }
    return ans;}
};
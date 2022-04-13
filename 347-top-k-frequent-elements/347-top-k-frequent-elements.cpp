class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> map;
        vector<int> ans;
       
        for(int i:nums){
            if(map.find(i)==map.end())map.insert(make_pair(i,1));
            else{
                map[i]++;
            }
        }
        
       vector<pair<int,int>> tempans=sortmap(map);
        
        for(int i=0;i<k;i++){
            ans.push_back(tempans[i].first);
        }
        
        return ans;
        
        
    }
    
    // bool sortbyval(pair<int,int>&a,pair<int,int>&b){
    //     return a.second<b.second;
    // };
    
   vector<pair<int,int>> sortmap(unordered_map<int,int>&m){
       
       
        
        vector<pair<int,int>> temp;
        for(auto& i:m){temp.push_back(i);}
       
       
        
        sort(temp.begin(),temp.end(),[](pair<int,int>&a,pair<int,int>&b)->bool{
        return a.second>b.second;
    });
       
       return temp;
        
        
        
    }
};
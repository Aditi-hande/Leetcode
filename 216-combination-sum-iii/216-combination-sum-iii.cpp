class Solution {
public:
    
    vector<vector<int>> combinationSum3(int k, int n) {
        vector<vector<int>> ans;
        vector<int> temp;
        helper(k,n,ans,temp);
        return ans;
        
        
        
    }
    
   void helper(int k,int n, vector<vector<int>>& ans, vector<int>temp){
       
      if(n==0 && temp.size()==k){ans.push_back(temp); return;}
       
       if(temp.size()<k){
           for(int i= temp.empty()? 1:temp.back()+1;i<=9;i++){
               if(n-i< 0)break;
               temp.push_back(i);
               helper(k,n-i,ans,temp);
               temp.pop_back();
           }
           
       }
   }
};
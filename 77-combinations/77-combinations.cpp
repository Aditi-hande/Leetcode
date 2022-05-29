class Solution {
public:
    vector<vector<int>>ans;
    void helper(int& n,int& k, int curridx,vector<int> currans){
        
        if(currans.size()>k)return;
        
        if(currans.size()==k){
            ans.push_back(currans);
            return;
        }
        
        for(int i=curridx;i<=n;i++){
            currans.push_back(i);
            helper(n,k,i+1,currans);
            currans.pop_back();
        }
        
    }
    
    vector<vector<int>> combine(int n, int k) {
        
        
        vector<int> currans;
        
        helper(n,k,1,currans);
        
        return ans;
                
    }
};
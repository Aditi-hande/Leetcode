class Solution {
public:
    
    void helper(int& n,int& k, int curridx, int currlen,vector<int> currans, vector<vector<int>>& ans){
        
        if(currlen>k)return;
        
        if(currlen==k){
            ans.push_back(currans);
            return;
        }
        
        for(int i=curridx;i<=n;i++){
            currans.push_back(i);
            currlen++;
            helper(n,k,i+1,currlen,currans,ans);
            currans.pop_back();
            currlen--;
        }
        
    }
    
    vector<vector<int>> combine(int n, int k) {
        
        vector<vector<int>>ans;
        vector<int> currans;
        
        helper(n,k,1,0,currans,ans);
        
        return ans;
                
    }
};
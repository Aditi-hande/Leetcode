class Solution {    
void combisum(vector<int>& candidates, int target, vector<int>currcomb, int currsum,int index,vector<vector<int>>& ans)
    {
        //check if sum is more
        if(currsum>target)return;
        
        //check if condition has reached
        if(currsum==target) {ans.push_back(currcomb); 
                             return;}
        
        //if sum is less
        
        for(int i=index;i<candidates.size();i++){
            
            //to avoid repetititon (different from combisum1)
            
            if(i>index && candidates[i]==candidates[i-1]) continue;
            if(candidates[i]>target)continue;
            currsum+=candidates[i];
            currcomb.push_back(candidates[i]);
            //cout<<currsum<<" ";
           // i++;
            combisum(candidates,target,currcomb,currsum,i+1,ans); 
            currcomb.pop_back();
            currsum-=candidates[i];
            
        }    
    }
    
    
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        
            vector<vector<int>> ans;

        vector<int>currcomb;
        sort(candidates.begin(),candidates.end());
        combisum(candidates,target,currcomb,0,0,ans);
        //ans.erase( unique( ans.begin(), ans.end() ), ans.end() );
        return ans;
        
    }
    
    
};
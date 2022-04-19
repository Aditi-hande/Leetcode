class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        
        vector<vector<int>> merged;
		if(intervals.size() == 0)
			return merged;
		sort(intervals.begin(), intervals.end());
        
        for(auto it:intervals){
            cout<<it[0]<<it[1]<<" ";
        }
        
		vector<int> temp;
		temp = intervals[0];
		for(auto it: intervals){
			if(it[0]<=temp[1])
				temp[1] = max(temp[1], it[1]);
			else{
				merged.push_back(temp);
				temp = it;
			}
		}
		merged.push_back(temp);
		return merged;
	}
        
    
};
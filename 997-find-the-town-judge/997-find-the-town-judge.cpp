class Solution {
public:
    int findJudge(int n, vector<vector<int>>& trust) {
        vector<int> h(n+1,0);
        for(auto i:trust)
            h[i[0]]--,h[i[1]]++;       // Calculating the indegree - outdegree
        for(int i=1;i<n+1;i++)
            if(h[i]==n-1)return i;        // finding for which point, indegree-outdegree  is n-1
        return -1;
    }
};
class Solution {
public:
    int findCenter(vector<vector<int>>& edges) {
         int n=edges.size()+1;
        vector<int>h(n+1,0);
       //cout<<n;
        for(auto i:edges){
            h[i[0]]++;
            h[i[1]]++;
        }
        for(int i=0;i<n+1;i++){
            //cout<<i;
            if(h[i]==n-1)return i;
            
        }
   return -1; }
};
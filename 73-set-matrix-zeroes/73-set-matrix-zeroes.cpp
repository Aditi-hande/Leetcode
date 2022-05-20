class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        
        //note that improvement to previous is that we dont need multiple array inputs as unique will make sure all in same row or col will be 0 so vector is changed to set
        
        vector<pair<int,int>> zero;
        set<int> row_set ;
    set<int> col_set ;
        for(int i=0;i<matrix.size();i++){
            for(int j=0;j<matrix[0].size();j++){
                
                if(matrix[i][j]==0) {
                    row_set.insert(i);
                    col_set.insert(j);
                }
                
            }
        }
        
       
            

        for(int i=0;i<matrix.size();i++){
            for(int j=0;j<matrix[0].size();j++){
                
                if (row_set.count(i) || col_set.count(j)) {
          matrix[i][j] = 0;
        }
                
            }
        }
            
            
        
 
        
    }
};
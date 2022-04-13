class Solution {
public:
    void reverseString(vector<char>& s) {
        
        int n=s.size();
        char temp;
        int low=0;
        int high=n-1;
        
        while(low<=high){
                temp=s[high];
                s[high]=s[low];
                s[low]=temp;
                low++;
                high--;
            }
        
//         if(n%2==0){
//             while(low<=high){
//                 temp=s[high];
//                 s[high]=s[low];
//                 s[low]=temp;
//                 low++;
//                 high--;
//             }
            
            
//         }
//         else{
//             while(low<=high){
                
//             }
            
//         }
        
    }
};
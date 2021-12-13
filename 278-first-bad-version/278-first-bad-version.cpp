// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
         int high,mid,low;
        high=n;
        low=1;
        
        if(isBadVersion(low)){return low;}
        
        while(low<high){
            mid=low+(high-low)/2;
           
            
            if(isBadVersion(mid)){high=mid;}
            else{
                 low = mid + 1;
                }
        }
   return low; }
       
};
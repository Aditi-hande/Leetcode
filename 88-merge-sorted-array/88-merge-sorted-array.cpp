class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
       int i=m+n-1;
    // first positon  of nums2
  int j= 0;
  
    // while i>=m and j<=n put nums2 in nums1
  while(i>=m && j<=n)

  {
      nums1[i] = nums2[j];
      i--;
      j++;
  }
    // now simply sort the nums1
  sort(nums1.begin(), nums1.end());
 
    }
};
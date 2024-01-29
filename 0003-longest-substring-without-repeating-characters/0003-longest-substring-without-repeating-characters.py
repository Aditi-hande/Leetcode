class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if not s:
            return 0
        if len(s)==1:
            return 1
        
        l=0
        r=1
        ctr=Counter(s[0])
        ans=1
        mans=1
        
        while(r<len(s)):
            # print(l,r,ans,mans)
            if s[r] in ctr and ctr[s[r]]==0 or s[r] not in ctr:
                ctr[s[r]]+=1
                ans+=1
                mans=max(mans,ans)
                r+=1
            else:
                ctr[s[r]]+=1
                ans+=1
                while(ctr[s[r]]!=1):
                    ctr[s[l]]-=1
                    l+=1
                    ans-=1
                r+=1
                # print(l,r,ans,mans)
                
        return mans
                    
                    
                    
                
                
                
            
            
        
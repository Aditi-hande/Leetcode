class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        ctr=Counter(ages)
        ans=0
        for age in ctr: #max 120
            for otherage in ctr:
                if otherage<=0.5*age+7: continue
                if otherage>age: continue
                if otherage==age:
                    ans+=ctr[age]*(ctr[age]-1)
                    continue
                ans+=ctr[age]*ctr[otherage]
                
                
        return ans
                
                    
                

        
        
            
        
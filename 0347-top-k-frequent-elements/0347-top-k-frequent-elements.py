class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        mp=Counter(nums)
        # print(mp)
        heap=[]
        ans=[]
        
        for num in mp.keys():
            if len(heap)>=k:
                heapq.heappushpop(heap,(mp[num],num))
            else:
                heapq.heappush(heap,(mp[num],num))
            # print(heap)
                
        while heap:
            ans.append(heapq.heappop(heap)[1])
        
        return ans
                
            
        
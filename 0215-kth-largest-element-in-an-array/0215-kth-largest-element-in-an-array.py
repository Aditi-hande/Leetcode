import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        heap=[]
        heapq.heappush(heap,nums[0])
        # print(heap)
        for i in range(1,len(nums)):
            if len(heap)<k:
                heapq.heappush(heap,nums[i])
                # print(heap)
            elif nums[i]>heap[0]:
                heapq.heappushpop(heap,nums[i])
                # print(heap)
        # print(heap)
        return heap[0]
        
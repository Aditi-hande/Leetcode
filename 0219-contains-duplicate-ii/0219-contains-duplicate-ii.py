class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #basically store number and its last found index
        map={}

        for i in range(len(nums)):
            if nums[i] in map and abs(map[nums[i]]-i)<=k:
                return True
            map[nums[i]]=i
        return False
        
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False

        # 0: -1 is for edge case that current sum mod k == 0
        # for when the current running sum is cleanly divisible by k
        # e.g: nums = [4, 2], k = 3
        sums = {0: -1}  # 0
        cumulative_sum = 0
        for idx, num in enumerate(nums):
            cumulative_sum += num
            remainder = cumulative_sum % k

            # if current_sum mod k is in dict and index idx - sums[remainder] > 1, we got the Subarray!
            # we use 2 not 1 because the element at sums[remainder] is not in the subarray we are talking about
            if remainder in sums and idx - sums[remainder] >= 2:
                return True

            # if current sum mod k not in dict, store it so as to ensure the further values stay
            if remainder not in sums:
                sums[remainder] = idx
        
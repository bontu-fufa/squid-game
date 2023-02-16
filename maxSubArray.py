class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        prev = nums[0]
        
        for i in range(1,len(nums)):
            curr_sum = nums[i] + prev
            curr_max = max(nums[i],curr_sum)
            max_sum= max(max_sum, curr_max)
            prev = curr_max
        return max_sum

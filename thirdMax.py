class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(set(nums))
        nums.sort()

        if len(nums) > 2: return nums[-3]
        return nums[-1]

class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        start,end = 0,len(nums) - 1
        squared = [None] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            if abs(nums[start]) >= abs(nums[end]):
                squared[i] = nums[start]**2
                start+=1
            else:
                squared[i] = nums[end]**2
                end-=1
                
        return squared

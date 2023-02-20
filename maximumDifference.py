class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j = 1
        min_num = nums[0]
        res = -1
        while j < len(nums):
            num = nums[j]
            if num > min_num: 
                res = max(res,num - min_num)
            else: min_num = num
            j+=1
        return res

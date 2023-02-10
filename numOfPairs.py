class Solution(object):
    def numOfPairs(self, nums, target):
        """
        :type nums: List[str]
        :type target: str
        :rtype: int
        """
        count = 0
        length = len(nums)
        for i in range(length):
            for j in range(i+1,length):
                if (nums[i] + nums[j] == target):
                    count+=1
                if (nums[j] + nums[i] == target):
                    count+=1
        return count
        

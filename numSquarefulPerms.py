class Solution(object):
    def dfs(self,nums, prev):
        if not nums: return 1
        
        res = 0
        for i, num in enumerate(nums):
            if i and num == nums[i - 1]: continue
            s = num + prev
            if prev < 0 or int(sqrt(s))**2 == s:
                res += self.dfs(nums[:i] + nums[i+1:], num)
        return res
    def numSquarefulPerms(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
       
        nums = sorted(nums)
        if not nums: return 0
        return self.dfs(nums, -1) 

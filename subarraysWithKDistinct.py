class Solution(object):
    def distnict(self, nums, k):
        dict = defaultdict(int)
        left = 0
        right = 0
        res = 0
        while right < len(nums):
            dict[nums[right]] += 1
            while len(dict) > k:
                dict[nums[left]] -= 1
                if dict[nums[left]] == 0:
                    del dict[nums[left]]
                left += 1
            res += right - left + 1
            right += 1
        return res
    def subarraysWithKDistinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.distnict(nums, k) - self.distnict(nums, k - 1)

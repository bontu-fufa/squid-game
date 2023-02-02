class Solution(object):
    def numberOfWays(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        all_ones = sum([int(c) for c in s])
        all_zeros = n - all_ones
        pre_zeros = 1 if s[0] == '0' else 0 
        pre_ones = 1 - pre_zeros
    
        ways = 0
        for i in range(1, n-1):
            if s[i] == '0':
                pre_zeros += 1
                ways += pre_ones * (all_ones - pre_ones)
            else:
                pre_ones += 1
                ways += pre_zeros * (all_zeros - pre_zeros)
                
        return ways

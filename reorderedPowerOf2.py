class Solution(object):
    def reorderedPowerOf2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        n_count = Counter(str(n))
        
        for i in range(30):
            p = 2**i
            powered_count = Counter(str(p))
            if powered_count == n_count: return True
        
        return False

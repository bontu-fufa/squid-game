class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = list(str(num))
        n = len(num)
        for i in range(n-1):                                
            if num[i] < num[i+1]: break
        else: return int(''.join(num))

        idx, max_num = i+1, num[i+1]   
        for j in range(i+1, n):
            if max_num <= num[j]: idx, max_num = j, num[j]
        
        left = i                                        
        for j in range(i, -1, -1):    
            if num[j] < max_num: left = j

        num[idx], num[left] = num[left], num[idx]   
        return int(''.join(num))  

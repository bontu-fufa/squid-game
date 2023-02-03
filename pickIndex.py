class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.w = w
        self.total = sum(self.w)
        
        for i in range(1,len(w)):
            self.w[i] += self.w[i-1]
        

    def pickIndex(self):
        """
        :rtype: int
        """
        random_num = random.random() * self.total
        
        left, right = 0, len(self.w)-1
        
        while left < right:
            mid = (left + right) // 2
            if self.w[mid] < random_num:
                left = mid + 1
            else: right = mid
    
        return  left  

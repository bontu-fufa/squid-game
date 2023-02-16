class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 == 1: return []
        
        nums_frequency = collections.defaultdict(int)
        for num in changed: 
            nums_frequency[num] += 1 
        
        original = []
        changed.sort()
        for num  in changed: 
            if nums_frequency[num] == 0 : continue
            
            if num == 0: 
                if nums_frequency[0] % 2 == 1 : return []
                frequency = nums_frequency[0]
                zeros = [0] * (frequency // 2)
                original += zeros
                nums_frequency[0] = 0
                
            if num*2 in nums_frequency and nums_frequency[num*2] > 0: 
                original.append(num)
                nums_frequency[num] -= 1 
                nums_frequency[num*2] -= 1
               
        if len(original) != len(changed)//2: 
            return []
                
        return original

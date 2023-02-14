class Solution:
    def sumZero(self, n: int) -> List[int]:
        
        neg = []
        if n == 1:
            return [0]
        
        num = n
        for i in range(n//2):
            neg.append((-(num-i)))
        # print(negatives)
        pos = []
        
        for i in range(n//2):
            pos.append(-(neg[i]))
        if n%2 == 0:
            # print(len(pos + neg))
            return pos + neg
        else :
            # print(len(pos + neg+[0]))
            return pos + neg  + [0]
        
        # print(answe/r)

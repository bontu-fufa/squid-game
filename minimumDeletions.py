class Solution(object):
    def minimumDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        deletions = 0
        stack = []
        
        for ch in s:
            if ch == "a":
                if stack:
                    stack.pop()
                    deletions += 1
            else: stack.append(ch)
                
        return deletions

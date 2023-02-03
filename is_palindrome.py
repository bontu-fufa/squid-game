class Solution(object):
    def is_palindrome(self,word):
        if len(word) < 2 : return True
        left = 0 
        right = len(word) - 1
        while left <= right: 
            if word[left] != word[right]: return False 
            left += 1
            right -= 1
        return True
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """        
        left = 0 
        right = len(s) - 1
        mismatch = 0 
        while left <= right : 
            if s[left] != s[right]: 
                mismatch += 1
                break 
            left += 1
            right -= 1
        # print(left,right)
        if mismatch == 1: 
            left_removed = self.is_palindrome(s[left+1:right+1])
            right_removed = self.is_palindrome(s[left:right])
            # print(left_removed,right_removed)
            if not (left_removed or right_removed): return False
        return True

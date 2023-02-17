class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        p = []

        def generate(parentheses, left, right):
            if len(parentheses) == 2*n:
                p.append(parentheses)
                return
            
            if left < n:
                generate(parentheses+"(", left+1, right)

            if left > right:
                generate(parentheses+")", left, right+1)

        generate("", 0, 0)

        return p

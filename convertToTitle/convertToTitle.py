class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        res = ""
        while columnNumber > 0 :   

            columnNumber -= 1
            res += chr( (columnNumber % 26) + 65 )
            columnNumber //= 26

        return res[::-1]  

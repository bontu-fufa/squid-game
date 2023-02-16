class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        symbol_value_map= {"I":1,"V": 5,"X":10,"L":50,"C":100,"D":500,"M": 1000}
        value = 0;
        for i in range (len(s)):
            if i < len(s) - 1 and symbol_value_map[s[i]] < symbol_value_map[s[i+1]]:
                    value -= symbol_value_map[s[i]]
            else:
                value += symbol_value_map[s[i]]
        return value

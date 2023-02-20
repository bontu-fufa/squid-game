class Solution(object):
    def validIPAddress(self, queryIP):
        """
        :type queryIP: str
        :rtype: str
        """
        def isIPv4(val):
            if not val.isdecimal(): return False
            if val[0] == "0" and len(val) > 1:   return False
            if 0 < int(val) > 255:   return False
            return True
     
        def isIPv6(val):
            if len(val) > 4 or len(val) == 0:
                    return False
            hex_char = {"a","b","c","d","e","f","A","B","C","D","E","F"}
            for v in val:
                if not (v.isdecimal() or v in hex_char): return False
            return True

        if queryIP.count(".") == 3 and all(isIPv4(query) for query in queryIP.split(".")): return "IPv4"
        elif queryIP.count(":") == 7 and all(isIPv6(query) for query in queryIP.split(":")): return "IPv6"
    
        return "Neither"

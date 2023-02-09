class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n = len(s) 
        ans = set()       
        def func(idx, arr):
            if idx == len(s):
                if len(arr) == 4: 
                    ans.add(".".join(arr))
                return
            
            if s[idx] == "0":
                func(idx+1, arr+["0"])
                return
            
            for i in range(idx, n):
                if int(s[idx:i+1]) < 256:
                    func(i+1, arr+[s[idx:i+1]])
                else:
                    break
        func(0, [])
        return ans

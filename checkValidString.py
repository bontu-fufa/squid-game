class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        par = []
        star = []
        
        for i, x in enumerate(s):
            if x == "(": par.append(i)
            if x == ")":
                if par:  par.pop()
                elif star: star.pop()
                else: return False
            if x == "*": star.append(i)
        
        while par and star:
            par_index = par.pop()
            star_index = star.pop()
            if par_index < star_index: continue
            else: return False
            
        return not par

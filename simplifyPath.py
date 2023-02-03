# 71. Simplify Path
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        res=[]
        for folder_name in path.split("/"): 
            if folder_name == ".." and res: res.pop()
            if folder_name not in [".", "..", ""]: 
                res.append(folder_name)
                
        return "/" + "/".join(res)

class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        l = len(pref)
        count = 0
        for word in words: 
            if len(word) < l: continue
            if word[:l] == pref: count += 1
        return count

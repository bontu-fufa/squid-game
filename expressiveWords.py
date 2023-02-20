class Solution(object):
    def expressiveWords(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: int
        """
        s_group = [[key, len(list(group))] for key, group in itertools.groupby(s)]
        res = 0
        for word in words:
            word_group = [[key, len(list(group))] for key, group in groupby(word)]
            if (len(s_group) == len(word_group) and  all(s_g[0] == w_g[0] and (s_g[1] == w_g[1] or s_g[1] > w_g[1] and s_g[1] >= 3)
                    for s_g, w_g in zip(s_group, word_group))):
                res += 1
        return res 

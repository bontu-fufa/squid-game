class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        curr = []
        ans = []
        n = 0
        for word in  words: 
            while len(word) + n + len(curr) > maxWidth:
                gaps = len(curr) - 1 or 1
                que, rem = divmod(maxWidth - n, gaps)
                for i in range(gaps):
                    curr[i] += ' '*que+(' ' if i < rem else '')
                ans.append(''.join(curr))
                n,curr = 0,[]
            curr.append(word)
            n += len(word)
        return ans + [" ".join(curr).ljust(maxWidth)] if curr  else []

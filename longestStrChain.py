class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        if len(words) == 0:
            return 0
    
        words_dict = {}
        words = sorted(words, key = lambda x: len(x))
        for word in words:
            is_chain = False
            for i in range(len(word)):
                search = word[:i] + word[i+1:]
                if search in words_dict:
                    words_dict[word] = max(words_dict.get(word, 0), words_dict[search] + 1)
                    is_chain = True
                
                if not is_chain:
                    words_dict[word] = 1
        
        return max(words_dict.values())

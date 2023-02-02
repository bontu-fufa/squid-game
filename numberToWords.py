class Solution(object):
    def __init__(self): 
        self.tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy","Eighty", "Ninety"]
        self.less_than_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight","Nine", "Ten","Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen","Sixteen", "Seventeen", "Eighteen", "Nineteen"]

    def change_to_word(self,num):
            if num<20:
                word = self.less_than_20[num]
            elif num<100:
                word = self.tens[num//10] + " " + self.less_than_20[num%10]
            elif num<1000:
                word = self.change_to_word(num//100) + " Hundred " + self.change_to_word(num%100)
            elif num<1000000:
                word = self.change_to_word(num//1000) + " Thousand " + self.change_to_word(num%1000)
            elif num<1000000000:
                word = self.change_to_word(num//1000000) + " Million " + self.change_to_word(num%1000000)
            else:
                word = self.change_to_word(num//1000000000) + " Billion " + self.change_to_word(num%1000000000)
            return word.strip()
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num==0: return "Zero"
        return self.change_to_word(num)

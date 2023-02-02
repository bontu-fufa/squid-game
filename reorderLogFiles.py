class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        letter_logs = []
        digit_logs = []
        
        for log in logs:
            first , content = log.split(" ", 1)
            if content[0].isdigit(): 
                digit_logs.append(log)
            else:
                letter_logs.append(log)
        
        letter_logs.sort(key=lambda log: (log.split(' ')[1:], log.split(' ')[0]))
        return letter_logs + digit_logs
        

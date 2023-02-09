class Solution(object):
    def reformatDate(self, date):
        """
        :type date: str
        :rtype: str
        """
        date_info = date.split()
        months = {"Jan":"01", "Feb":"02", "Mar":"03", "Apr":"04", "May":"05", "Jun":"06", "Jul":"07", "Aug":"08", "Sep":"09", "Oct":"10", "Nov":"11", "Dec":"12"}
        
        if int(date_info[-3][:-2]) < 10:
            date_info[-3] = "0"+date_info[-3]
        return date_info[-1]+"-"+months[date_info[-2]]+"-"+date_info[-3][:-2]

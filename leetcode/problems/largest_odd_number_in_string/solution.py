class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        
        print(num[:-2])
        for i in range(1,len(num)+1):
                if int(num[-i])%2!=0 and i==1:
                    return num[:]
                elif int(num[-i])%2!=0:
                    return num[:-i+1]
                else:
                    continue
        return ""


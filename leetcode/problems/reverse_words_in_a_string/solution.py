class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        l=s.split()
        m=l[-1]
        for i in range(2,len(l)+1):
            m+=" "+l[-i]
        
        return m

        
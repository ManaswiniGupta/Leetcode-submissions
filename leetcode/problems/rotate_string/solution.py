class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        k=""
        if len(s)!=len(goal):
            return False
        for i in range(len(s)):
            k=s[i:]+s[:i]
            
            if k==goal:
                return True
        return False
        
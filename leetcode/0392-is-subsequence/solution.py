class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s)==0:
            return True 
        ps=0
        pr=0
        while ps<len(s) and pr < len(t):
            if s[ps]==t[pr]:
                ps+=1
            pr+=1
        if ps==len(s):
            return True 
        return False
        

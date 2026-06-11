class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        w=s.split(" ")
        if len(pattern)!=len(w):
            return False
        if len(set(pattern)) != len(set(w)):
            return False
        d={}
        for i in range(len(pattern)):
            if pattern[i] not in d.keys():
                d[pattern[i]]=w[i]
            elif  pattern[i] in d.keys() and d[pattern[i]]!=w[i]:
                return False
        return True
        
